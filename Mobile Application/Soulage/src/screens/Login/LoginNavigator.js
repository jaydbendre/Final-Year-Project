import React from 'react';

// For Navigation
import { createStackNavigator } from 'react-navigation-stack';

// For Screens
import LoginScreen from './LoginScreen';
import RegisterScreen from './RegisterScreen';

const navigator = createStackNavigator({
    LoginScreen: {
        screen: LoginScreen
    },
    RegisterScreen: {
        screen: RegisterScreen
    }
}, {
    initialRouteName: 'LoginScreen'
});

export default navigator;