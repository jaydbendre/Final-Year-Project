import React, { useState } from 'react';
import { Text, View, StyleSheet, TouchableOpacity } from 'react-native';

import { withNavigation } from 'react-navigation';

// For Progress Bar
import { Bar } from 'react-native-progress';

// For UPI Payment
import UpiPayment from '../services/UpiPayment';

// For PopUp Input
import DialogInput from 'react-native-dialog-input';

// API
import SoulageApi from '../api/mainApi';


const DescriptionCard = ({ request_id, description, sponsor }) => {
    // const id = navigation.getParam('id');
    const [visible, setVisible] = useState(false);
    const [amount, setAmount] = useState(0);

    const onPayment = (data) => {
        if(data["STATUS"] === "SUCCESS"){
            console.log("Payment Success");
            // Make API call to submit the detail of transaction
        }
    }

    const payUsingUPI = async (amt) => {
        // UpiPayment()
        setVisible(false);
        console.log(amt);
        try{
            await UpiPayment({ amount: amt, onPayment: onPayment });
            setAmount(amt);
        } catch(err){
            console.log(err);
        }
    }

    const dialogBox = () => {
        setVisible(true);
    }

    
    return(
        <>
        <DialogInput
            isDialogVisible={visible}
            title={"Donation"}
            message={"Enter Amount in Rupees"}
            hintInput={"100"}
            submitInput={(amt) => payUsingUPI(amt)}
            closeDialog={ () => setVisible(false)}
        >
        </DialogInput>
        <View style={styles.container}>
            <Text style={styles.descText}>Description:</Text>
            <Text>{description}</Text>
            <Text style={[styles.descText, { marginTop: '2%' }]}>Backed By: {sponsor}</Text>
            <View style={styles.bottom}>
                <View style={{ flexDirection: 'column', alignContent: 'center' }}>
                    <Text>Requirements Collected</Text>
                    <Bar progress={0.7} width={200} height={10} />
                </View>
                <TouchableOpacity style={styles.button} onPress={dialogBox}>
                    <Text style={styles.buttonText}>Donate</Text>
                </TouchableOpacity>
            </View>
        </View>
        </>
        // <Bar progress={0.7} width={200} />
    )
}

/*
class DescriptionCard extends React.Component {
    constructor(props){
        super(props);
        this.state = {
            visible: false,
            amount: 0
        }
        this.req_id = this.props.navigation.getParam('id'),
        this.name = this.props.navigation.getParam('name')
    }

    componentDidMount(){
        this.getData();
    }

    getData = async () => {
        try{
            const response = await SoulageApi.get(`get_donations/${this.name}`);
            console.log(response.data[0]);
            // this.setState({
            //     items: response.data,
            //     loading: false
            // })

        } catch(err){
            console.log(err);
            this.setState({ loading: false });
        }
    }

    onPayment = (data) => {
        if(data["STATUS"] === "SUCCESS"){
            console.log("Payment Success");
            // Make API call to submit the detail of transaction
        }
    }

    payUsingUPI = async (amt) => {
        // UpiPayment()
        setVisible(false);
        console.log(amt);
        try{
            await UpiPayment({ amount: amt, onPayment: this.onPayment });
            setAmount(amt);
        } catch(err){
            console.log(err);
        }
    }

    dialogBox = () => {
        this.setState({
            visible: true
        })
    }

    render(){
        return(
            <>
                <DialogInput
                    isDialogVisible={this.state.visible}
                    title={"Donation"}
                    message={"Enter Amount in Rupees"}
                    hintInput={"100"}
                    submitInput={(amt) => this.payUsingUPI(amt)}
                    closeDialog={ () => this.setState({ visible: false})}
                >
                </DialogInput>
                <View style={styles.container}>
                    <Text style={styles.descText}>Description:</Text>
                    <Text>{description}</Text>
                    <Text style={[styles.descText, { marginTop: '2%' }]}>Backed By: {sponsor}</Text>
                    <View style={styles.bottom}>
                        <View style={{ flexDirection: 'column', alignContent: 'center' }}>
                            <Text>Requirements Collected</Text>
                            <Bar progress={0.7} width={200} height={10} />
                        </View>
                        <TouchableOpacity style={styles.button} onPress={this.dialogBox}>
                            <Text style={styles.buttonText}>Donate</Text>
                        </TouchableOpacity>
                    </View>
                </View>
            </>
            // <Bar progress={0.7} width={200} />
        )
    }
}
*/

DescriptionCard.defaultProps = {
    description: 'The flooding in Chennai city was described as the worst in a century. The continued rains led to schools and colleges remaining closed across Puducherry and Chennai, Kancheepuram and Tiruvallur districts in Tamil Nadu, and fishermen were warned against sailing because of high waters and rough seas.',
    sponsor: 'Robert Bosch',
    request_id: 1,
}

const styles = StyleSheet.create({
    container: {
        flexDirection: 'column',
        justifyContent: 'space-between',
        elevation: 5,
        marginHorizontal: 10,
        marginVertical: 15,
        paddingVertical: 15,
        paddingHorizontal: 10,
        backgroundColor: '#FFFFFF',
    },
    descText: {
        fontSize: 15,
        fontWeight: 'bold'
    },
    bottom: {
        flexDirection: 'row',
        justifyContent: 'space-between',
        alignItems: 'center',
        marginTop: '5%',
    },
    button: {
        borderWidth: 1,
        borderRadius: 5,
        paddingHorizontal: 10,
        paddingVertical: 5,
        backgroundColor: 'blue',
    },
    buttonText: {
        color: 'white',
        textAlignVertical: 'center'
    }
});

export default withNavigation(DescriptionCard);