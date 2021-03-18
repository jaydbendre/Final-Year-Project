import React from 'react';
import { Text, View, ScrollView, StyleSheet } from 'react-native';

// For Navigation
import { withNavigation } from 'react-navigation';

// Loader
import AnimatedLoader from '../Spinner/spinner';

// Header
import Header from '../Components/Header';

import DescriptionCard from '../Components/DescriptionCard';

// API
import SoulageApi from '../api/mainApi';

class DisasterDescription extends React.Component {
    constructor(props){
        super(props);
        this.state = {
            items: [],
            loading: true
        }
        this.request_id = this.props.navigation.getParam('id');
        this.name = this.props.navigation.getParam('name');
    }

    static navigationOptions = {
        headerTitle: () => {
            return(
                <Header navOption={false} />
            )
        }
    }

    componentDidMount(){
        this.getData();
    }

    getData = async () => {
        try{
            const response = await SoulageApi.get(`get_donations/${this.name}`);
            // console.log(response.data);
            this.setState({
                items: response.data,
                loading: false
            })

        } catch(err){
            console.log(err);
            this.setState({ loading: false });
        }
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

    renderItems = () => {
        if(this.state.items.length == 0){
            return (
                <View style={{ justifyContent: 'center', alignItems: 'center' }}>
                    <Text>
                        No Data Available to Render
                    </Text>
                </View>
            )
        }else{
            return this.state.items.map((item, num) => {
                return(
                    <DescriptionCard key={item.initiated_by} request_id={this.request_id} sponsor={item.initiated_by} />
                )
            })
        }
    }

    render(){
        
        return(
            <>
                {this.state.loading ? this.renderSpinner() :

                <ScrollView>
                    {this.renderItems()}
                    {/* <DescriptionCard request_id={request_id} />
                    <DescriptionCard request_id={request_id} sponsor={"JP Morgan"} />
                    <DescriptionCard request_id={request_id} sponsor={"Nomura"} />
                    <DescriptionCard request_id={request_id} sponsor={"Google"} />
                    <DescriptionCard request_id={request_id} sponsor={"Apple"} /> */}
                </ScrollView>
                }
            </>
        )
    }
}

const styles = StyleSheet.create({});

export default withNavigation(DisasterDescription);