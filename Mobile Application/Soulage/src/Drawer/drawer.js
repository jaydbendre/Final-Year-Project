import React from 'react';
import drawerNavigator from './customDrawer';
import MainScreen from '../screens/MainScreen';

import { createDrawerNavigator } from 'react-navigation-drawer';
import { createStackNavigator } from 'react-navigation-stack';

// import ProfileScreen from '../screens/Profile';
import DisasterListScreen from '../screens/DisasterList';
import DisasterDescScreen from '../screens/DisasterDescription';

import Header from '../Components/Header';

const drawer = createDrawerNavigator({
    dashBoard: {
        // screen: MainScreen
        screen: createStackNavigator({
            MainScreen: MainScreen,
            DisasterListScreen: DisasterListScreen,
            DisasterDescScreen: DisasterDescScreen,
        }, {
            defaultNavigationOptions: {
                headerTintColor: '#444',
                headerStyle: { backgroundColor: 'white', height: 60 },
                cardStyle: { backgroundColor: 'white' },
                headerTitle: () => (
                    <Header />
                )
            }
        })
    }
}, {
    drawerPosition: 'left',
    drawerWidth: '60%',
    contentComponent: drawerNavigator
});

export default drawer;