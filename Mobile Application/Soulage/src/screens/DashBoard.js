import React, { Component } from 'react';
import { Text, View, StyleSheet, Image, ScrollView } from 'react-native';
import Accordion from 'react-native-collapsible/Accordion';
// import FlipCard from 'react-native-flip-card';


// Components
import TweetCard from '../Components/TweetCard';
import TweetSentiment from '../Components/TweetSentiment';

// For API Call
import SoulageApi from '../api/mainApi';

// For Flash Message
import { showMessage } from 'react-native-flash-message';

// For Loader
import AnimatedLoader from '../Spinner/spinner';

import { Dimensions } from "react-native";
const screenWidth = Dimensions.get("window").width;


class Dashboard extends Component {
    constructor(props){
        super(props);
        this.state = {
            activeSections: [],
            sections: [],
            loading: true
        }
    }

    componentDidMount(){
        this.showMsg("Log in Successful")
        this.getData();
    }

    
    showMsg = (message) => {
        showMessage({
            message: message,
            // description: descp,
            type: 'info',
            autoHide: true,
            duration: 3000,
            position: 'bottom',
            floating: true,
            style: {
                backgroundColor: 'rgb(224, 224, 224)',
                width: '70%',
                alignSelf: 'center'
            },
            titleStyle: {
                color: 'black',
                textAlign: 'center',
            }
        });
    }

    getData = async () => {
        try{
            const response = await SoulageApi.get('mobapp/get_dashboard_data');
            // console.log(response.data);
            this.setState({
                sections: response.data,
                loading: false
            });
        } catch(err){
            console.log(err);
            this.setState({
                loading: false
            })
        }
    }

    _renderHeader = (section) => {
        // console.log(section.tweet_data.text);
        return (
            <View style={styles.headerView}>
                {/* <Text style={styles.headerText}>{"section.tweet_data"}</Text> */}
                <TweetCard tweet_text={section.tweet_data.text} />
            </View>
        )
    }

    _renderContent = (section) => {
        // console.log(section.chart_data);
        return(
            <View style={styles.content}>
                <TweetSentiment sentiment={section.chart_data} />
            </View>
        )
    }

    _updateSections = (activeSections) => {
        this.setState({ activeSections });
    }

    renderSpinner = () => {
        return (
            <AnimatedLoader
                visible={this.state.loading}
                overlayColor="rgba(255,255,255,0.75)"
                animationStyle={{ width: '100%', height: '100%' }}
                speed={1}
            />
        )
    }

    render() {
        if(this.state.loading){
            return(
                this.renderSpinner()
            )
        }else {
            return (
                <ScrollView style={styles.container}>
                    
                    <Accordion
                        sections={this.state.sections}
                        activeSections={this.state.activeSections}
                        // renderSectionTitle={this._renderSectionTitle}
                        renderHeader={this._renderHeader}
                        renderContent={this._renderContent}
                        onChange={this._updateSections}
                    />
                    
                </ScrollView>
            )
        }
    }
}

const styles = StyleSheet.create({
    container: {
        flex: 1
    },
    headerView: {
        justifyContent: 'flex-start',
        alignItems: 'flex-start',
        paddingVertical: '2%',
        height: 250,
        // borderWidth: 1,
        borderRadius: 3,
        elevation: 2,
        margin: 2
    },
    headerText: {
        flexDirection: 'row',
        alignSelf: 'center',
        justifyContent: 'center'
    },
    content: {
        justifyContent: 'center',
        alignItems: 'center'
    },
    heading: {
        fontSize: 25,
        fontWeight: 'bold',
        fontStyle: 'italic'
    },
    image: {
        width: '100%',
        height: '100%',
    }
});

export default Dashboard;