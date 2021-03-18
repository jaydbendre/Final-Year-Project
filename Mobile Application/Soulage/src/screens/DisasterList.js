import React from 'react';
import { Text, View, StyleSheet, ScrollView } from 'react-native';

// For Header
import Header from '../Components/Header';
import DisasterListCard from '../Components/DisasterListCard';
import DisasterCard from '../Components/DisasterListCard';

// Loader
import AnimatedLoader from '../Spinner/spinner';

// API
import SoulageApi from '../api/mainApi';

class DisasterList extends React.Component {
    constructor(props){
        super(props);
        this.state = {
            // items: ["Chennai Flood", "Hyderabad Floods", "Locust Infestation", "Ahmedabad Factory Blast", "Uttarakhand Forest Fire", "Dahej Chemical plant Expl", "Amphan Cyclone", "Assam Oil leak", "Kerala Flood"]
            items: [],
            loading: true
        };
    }

    static navigationOptions = {
        headerTitle: () => {
            return(
                <Header
                    navOption={false}
                />
            )
        }
    }

    componentDidMount(){
        this.getData();
    }

    getData = async () => {
        try{
            const response = await SoulageApi.get('get_topics');
            console.log(response.data);
            this.setState({
                items: response.data,
                loading: false
            })
            // this.setState({
            //     items: [response.data.topics[0], response.data.topics[1]],
            //     loading: false
            // });
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

    render() {
        return(
            <>
            {this.state.loading ? this.renderSpinner() : null}
            <ScrollView style={styles.container}>
                {this.state.items.map( item => {
                    return(
                        <View key={item.id}>
                            <DisasterListCard title={item} />
                        </View>
                    )
                })}
            </ScrollView>
            </>
        )
    }
}

const styles = StyleSheet.create({
    container: {
        flex: 1
    }
});

export default DisasterList;