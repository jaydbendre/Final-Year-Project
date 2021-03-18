import React, { useState, useContext, useEffect } from 'react';
import { Text, View, StyleSheet, NativeModules, TouchableOpacity } from 'react-native';
import { Input, Button } from 'react-native-elements';

// For Icons
import AntDesign from 'react-native-vector-icons/AntDesign';
import Feather from 'react-native-vector-icons/Feather';
import Octicons from 'react-native-vector-icons/Octicons';

// For Navigation
import { navigate } from '../../navigationRef';

// Context
import {Context as AuthContext} from '../../Context/AuthContext';

// Loader
import AnimatedLoader from '../../Spinner/spinner';
import { State } from 'react-native-gesture-handler';

// Flash Message
import { showMessage } from 'react-native-flash-message';
 
const { RNTwitterSignIn } = NativeModules;

// const TwitterCreds = {
//     "api_key": "oCmpLXRGbG2fLljIRJb0MHXan",
//     "secret_key": "F9k63Q18FwYrfgtUrvS2O820P9kvak3x7QEzVhhaooJXxsMDFp"
// }

// const TwitterCreds = {
//     "api_key": "hZO6gU344DJEi1mXKkJeDubci",
//     "secret_key": "FZ0WcumhDXaw6hkkQZRoqekIyVErcEaEYSBKcdeM2SoRU0hGqb"
// }

const TwitterCreds = {
    "api_key": "PmGdDoSbyICTvxbVmPgUThABb",
    "secret_key": "NbsjTWNISrrTDzSPkJ4z87iKTee3VvByP8FfwxH4dMIzBQE3z1"
}

// const TwitterCreds = {
//     "api_key": "oCmpLXRGbG2fLljIRJb0MHXan",
//     "secret_key": "F9k63Q18FwYrfgtUrvS2O820P9kvak3x7QEzVhhaooJXxsMDFp"
// }


const Twitter_SignIn = () => {
    RNTwitterSignIn.init(TwitterCreds["api_key"], TwitterCreds["secret_key"]);
    RNTwitterSignIn.logIn().then(loginData => {
        console.log(loginData);
        navigate('Dashboard');
        // const { authToken, authTokenSecret } = loginData;
        // if(authToken && authTokenSecret){
        //     console.log("Received Tokens Successfully...");

        //     // navigate('Dashboard');

        // }
    }).catch(err => {
        console.log("Twitter Key Error: ", err);
        navigate('Dashboard');
    });
    // const loginData

}

const TwitterLogOut = () => {
    RNTwitterSignIn.logOut();
    console.log("Logged Out Successfully");
}

const LoginScreen = () => {
    
    const [username, setUsername] = useState('');
    const [pwd, setPwd] = useState('');
    const [iconName, setIconName] = useState('eye');
    const [loading, setLoading] = useState(false);

    const { state, TwitterSignIn, signIn } = useContext(AuthContext);

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

    const normalSignIn = () => {
        setLoading(true);
        // console.log(username, pwd);

        if(username !== '' && pwd !== ''){
            
            signIn(username, pwd);
        }
    }

    const TweetSignIn = () => {
        // TwitterSignIn();
        Twitter_SignIn();
    }

    const renderLoader = () => {
        return (
            <AnimatedLoader
                visible={loading}
                overlayColor="rgba(255,255,255,0.75)"
                animationStyle={{ width: '100%', height: '100%' }}
                speed={1}
            />
        )
    }

    const showMsg = (message) => {
        showMessage({
            message: message,
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

    useEffect(() => {
        if(state.errormsg){
            console.log(state.errormsg);
            showMsg(state.errormsg);
        }

        if(loading){
            setLoading(false);
        }

    },[state.errormsg])

    return (
        <>
        {loading ? renderLoader(): null}
        <View style={styles.container}>
            {/* <View style={{ elevation: 5, borderWidth: 5, borderColor: 'white' }}>
                <Text style={styles.heading}>
                    Soulage
                </Text>
            </View> */}
            <TouchableOpacity style={styles.signupButton} onPress={() => navigate('RegisterScreen')}>
                <Text style={styles.signupText}>
                    Sign Up
                </Text>
            </TouchableOpacity>


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
                    onPress={normalSignIn}
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
                    onPress={() => TweetSignIn()}
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
        </>
    )
}

LoginScreen.navigationOptions = {
    headerTitle: () => (
        <View>
            <Text style={styles.heading}>
                Relevium
            </Text>
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
        marginTop: '20%',
    },
    signinButton: {
        marginHorizontal: 40
    },
    signupButton: {
        position: 'absolute',
        right: '5%',
        borderWidth: 1,
        marginLeft: 10,
        marginTop: 10,
        borderRadius: 10
    },
    signupText: {
        flexDirection: 'row',
        fontSize: 15,
        color: '#b5b5b5',
        justifyContent: 'center',
        alignItems: 'center',
        fontWeight: 'bold',
        margin: 5
    },
    text: {
        marginTop: 10,
        fontSize: 15,
        marginLeft: 10,
        textDecorationLine: 'underline'
    }
})

export default LoginScreen;