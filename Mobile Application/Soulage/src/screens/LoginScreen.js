import React, { useState } from 'react';
import { Text, View, StyleSheet, NativeModules, TouchableOpacity } from 'react-native';
import { Input, Button } from 'react-native-elements';

// For Icons
import AntDesign from 'react-native-vector-icons/AntDesign';
import Feather from 'react-native-vector-icons/Feather';
import Octicons from 'react-native-vector-icons/Octicons';

const { RNTwitterSignIn } = NativeModules;

const TwitterCreds = {
    "api_key": "oCmpLXRGbG2fLljIRJb0MHXan",
    "secret_key": "F9k63Q18FwYrfgtUrvS2O820P9kvak3x7QEzVhhaooJXxsMDFp"
}


const TwitterSignIn = () => {
    RNTwitterSignIn.init(TwitterCreds["api_key"], TwitterCreds["secret_key"]);
    RNTwitterSignIn.logIn().then(loginData => {
        console.log(loginData);
        const { authToken, authTokenSecret } = loginData;
        if(authToken && authTokenSecret){
            console.log("Received Tokens Successfully...");
        }
    }).catch(err => {
        console.log(err);
    });

}

const TwitterLogOut = () => {
    RNTwitterSignIn.logOut();
    console.log("Logged Out Successfully");
}

const LoginScreen = () => {
    
    const [username, setUsername] = useState('');
    const [pwd, setPwd] = useState('');
    const [load, setLoad] = useState('');
    const [iconName, setIconName] = useState('eye');

    const changeIcon = () => {
        if (iconName === "eye-closed"){
            setIconName('eye');
        }else{
            setIconName('eye-closed');

        }
    }
    const secure = () => {
        if (iconName === "eye"){
            return true;
        }else{
            return false;
        }
    }

    return (
        <View style={styles.container}>
            <View style={{ elevation: 5, borderWidth: 5, borderColor: 'white' }}>
                <Text style={styles.heading}>
                    Soulage
                </Text>
            </View>


            <View style={styles.signin}>
                <Input
                    label="Enter your Username"
                    placeholder="Ramesh"
                    value={username}
                    onChangeText={(val) => setUsername(val)}

                />

                <Input
                    label="Enter Your Password"
                    placeholder="Password"
                    value={pwd}
                    onChangeText={(val) => setPwd(val)}
                    rightIcon={
                        <TouchableOpacity onPress={changeIcon}>
                            <Octicons
                                name={iconName}
                                size={25}
                            />
                        </TouchableOpacity>
                    }
                    secureTextEntry={secure()}
                />
                
            </View>
            
            <View style={{ marginHorizontal: '20%' }}>
                <Button
                    title="Sign In"
                />
                <TouchableOpacity onPress={() => console.log("Forgot Password")}>
                    <Text style={styles.text}>Forgot Password?</Text>
                </TouchableOpacity>

                <Button
                    icon={
                        <AntDesign
                            name="twitter"
                            size={25}
                            color="#00acee"
                            style={{ paddingLeft: 5 }}
                        />
                    }
                    title="LogIn Using Twitter"
                    onPress={TwitterSignIn}
                    buttonStyle={{
                        backgroundColor: "transparent",
                    }}
                    titleStyle={{
                        color: "black",
                        paddingHorizontal: 10,
                    }}
                    containerStyle={{
                        borderColor: 'black',
                        borderWidth: 1,
                        borderRadius: 15,
                        marginTop: '10%',
                        marginHorizontal: '7%'
                    }}
                />
            </View>
        </View>
    )
}

const styles = StyleSheet.create({
    container: {
        justifyContent: 'flex-start'
    },
    heading: {
        justifyContent: 'center',
        alignItems: 'center',
        alignSelf: 'center',
        fontSize: 40,
        // fontFamily: 'sans-serif'
        fontStyle: 'italic'
    },
    signin: {
        marginTop: '15%',
    },
    signinButton: {
        marginHorizontal: 40
    },
    text: {
        marginTop: 10,
        fontSize: 15,
        marginLeft: 10,
        textDecorationLine: 'underline'
    }
})

export default LoginScreen;