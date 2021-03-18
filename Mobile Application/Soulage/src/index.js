import React from 'react';
import { Text, View, StyleSheet } from 'react-native';

import { createSwitchNavigator, createAppContainer } from 'react-navigation';

import { setNavigator } from './navigationRef';

import LoginFlow from './screens/Login/LoginNavigator';
import drawer from './Drawer/drawer';
import LoadingScreen from './screens/LoadingScreen';

// For Flash Message
import FlashMessage from 'react-native-flash-message';

// Reducers
import { Provider as AuthProvider } from './Context/AuthContext';

const switchnavigator = createSwitchNavigator({
    LoginFlow: {
        screen: LoginFlow
    },
    Dashboard: {
        screen: drawer
    },
    Loading: {
        screen: LoadingScreen
    }
}, {
    initialRouteName: 'LoginFlow'
});

const App = createAppContainer(switchnavigator);

export default () => {
    return(
        <AuthProvider>
            <App ref={(navigator) => setNavigator(navigator)} />
            <FlashMessage position="bottom" />
        </AuthProvider>
    )
}