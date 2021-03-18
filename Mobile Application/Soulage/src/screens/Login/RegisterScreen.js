import React, { useState, useEffect } from 'react';
import { Text, View, StyleSheet, TouchableOpacity, ScrollView } from 'react-native';
import { Input, CheckBox, Button } from 'react-native-elements';

// For Icons
import Octicons from 'react-native-vector-icons/Octicons';

// For Navigation
import { NavigationEvents } from 'react-navigation';

const RegisterScreen = () => {

    const [fName, setFname] = useState('');
    const [fnameErr, setfnameErr] = useState('');
    const [lName, setLname] = useState('');
    const [lnameErr, setlnameErr] = useState('');
    const [mobNumber, setMobNumber] = useState('');
    const [numErr, setnumErr] = useState('');
    const [dob, setDob] = useState('');
    const [dobErr, setdoberr] = useState('');
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [pwdErr, setpwdErr] = useState('');
    const [cBox, setcBox] = useState(false);
    const [loadIcon, setloadIcon] = useState(false);
    const [iconName, setIconName] = useState('eye');

    const changeIcon = () => {
        if (iconName === "eye-closed"){
            setIconName('eye');
        }else{
            setIconName("eye-closed");

        }
    }
    const secure = () => {
        if (iconName === "eye"){
            return true;
        }else{
            return false;
        }
    }
    const setMobileNumber = (val) => {
        let num = val[val.length-1];
        if(num === '.' || num === ',' || num === ' '){
            setMobNumber(mobNumber);
            return;
        }
        if(!isNaN(val[val.length-1])){
            setMobNumber(val)
        }else{
            setMobNumber(mobNumber);
        }
    }

    const checkInputs = () => {
        if(fName.length === 0){
            setfnameErr("First Name cannot be Empty");
            showMsg("First Name cannot be Empty");
            return false
        }
        if(lName.length === 0){
            setlnameErr("Last Name cannot be Empty");
            showMsg("Last Name cannot be Empty");
            return false
        }
        if(mobNumber.toString().length < 10){
            setnumErr("Enter a Valid Mobile Number");
            showMsg("Enter a Valid Mobile Number");
            return false;
        }
        if(address.streetName.toString().length === 0){
            setStreetErr('Enter Your Street Name');
            showMsg("Enter Your Street Name");
            return false;
        }
        if(address.areaCity.length === 0){
            setAreaErr('Enter your Area/City');
            showMsg("Enter Your Area/City Name");
            return false;
        }
        if(isNaN(address.pinCode)){
            console.log(isNaN(address.pinCode));
            setPinErr("Not a Valid Pin Code");
            showMsg("Not a Valid Pin Code");
            return false;
        }
        if(password.length === 0){
            setpwdErr("Password Cannot be Empty");
            showMsg("Password Cannot be Empty");
            return false;
        }
        return true;
    }

    const register = async() => {
        if(!checkInputs()){
            return null;
        }
        let data = {
            fname: fName,
            lname: lName,
            mobile_number: mobNumber,
            email: email,
            password,
        }

        setloadIcon(true);
        setTimeout(() => {
            setloadIcon(false);
        },10000);
        // signup(data);
    }

    const cbox = () => {
        if (cBox){
            setcBox(false);
        }else{
            setcBox(true);
        }
    }

    // const setDateofBirth = () => {
    //     if(dob){
    //         setDob(dob);
    //     }
    // }

    // useEffect(() => {
    //     // if(state.errorMsg){
    //     //     showMsg(state.errorMsg);
    //     //     removeError();
    //     // }
    //     if(loadIcon){
    //         setloadIcon(false);
    //     }
    // },[state.errorMsg]);

    return (
        <ScrollView style={styles.container}>
            {/* <NavigationEvents
                onWillBlur={removeError}
            /> */}
            <Text style={styles.text}>Welcome to Relevium!!!</Text>
            <Text style={styles.text}>Enter your details to Register.</Text>
            <View style={{ marginTop: 20 }} />

            <View style={{ marginLeft: 10 }}>
                <Input
                    label="First Name"
                    value={fName}
                    onChangeText={setFname}
                    placeholder="Rajesh"
                    errorMessage={fnameErr}
                />
                <Input
                    label="Last Name"
                    value={lName}
                    onChangeText={setLname}
                    placeholder="Singh"
                    errorMessage={lnameErr}
                />
                <Input
                    label="Date-of-Birth"
                    value={mobNumber}
                    // keyboardType={"numeric"}
                    onChangeText={setDob}
                    placeholder="dd-mm-yyyy"
                    maxLength={10}
                    errorMessage={dobErr}
                />
                <Input
                    label="Mobile Number"
                    value={mobNumber}
                    keyboardType={"numeric"}
                    onChangeText={setMobileNumber}
                    placeholder="9869125545"
                    maxLength={10}
                    errorMessage={numErr}
                />
                {/* <Input
                    label="Street Name"
                    value={address.streetName}
                    onChangeText={(val) => setAddress({ ...address, streetName: val})}
                    placeholder="Abc Street"
                    errorMessage={streetErr}
                />
                <Input
                    label="Area/City"
                    value={address.areaCity}
                    onChangeText={(val) => setAddress({ ...address, areaCity: val})}
                    placeholder="Ghatkopar(W), Mumbai"
                    errorMessage={areaErr}
                />
                <Input
                    label="Pin Code"
                    value={address.pinCode}
                    onChangeText={(val) => setAddress({ ...address, pinCode: val})}
                    placeholder="400012"
                    keyboardType={"numeric"}
                    errorMessage={pinErr}
                    maxLength={6}
                /> */}
                <Input
                    label="Email"
                    value={email}
                    onChangeText={setEmail}
                    placeholder="rajesh@gmail.com"
                />
                <Input
                    label="Password"
                    placeholder="Password"
                    rightIcon={
                        <TouchableOpacity onPress={changeIcon}>
                            <Octicons
                                name={iconName}
                                size={25}
                            />
                        </TouchableOpacity>
                    }
                    value={password}
                    onChangeText={setPassword}
                    secureTextEntry={secure()}
                    errorMessage={pwdErr}
                />
                
                <CheckBox
                    title="I agree to the TERMS & CONDITIONS"
                    checked={cBox}
                    onIconPress={cbox}
                    onPress={() => navigation.navigate('TermsConditionScreen')}
                />
                <View style={styles.registerButton}>
                    <Button
                        title="Register"
                        type="solid"
                        onPress={register}
                        disabled={!cBox}
                        loading={loadIcon}
                    />
                </View>
            </View>
        </ScrollView>
    )
}

const styles = StyleSheet.create({
    container: {
        marginTop: 20,
        marginRight: 15,
        marginBottom: 20,
        flex: 1,
        width: '100%',
        height: '100%'
    },
    text: {
        fontSize: 20,
        marginLeft: 20,
    },
    registerButton: {
        marginHorizontal: 40,
    }
});

export default RegisterScreen;