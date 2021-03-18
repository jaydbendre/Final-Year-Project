import React from 'react';
import { createBottomTabNavigator } from 'react-navigation-tabs';

import AntDesign from 'react-native-vector-icons/Entypo';
import Ionicons from 'react-native-vector-icons/Ionicons';
import MaterialIcons from 'react-native-vector-icons/MaterialIcons';

// For Screens
import DashBoard from './DashBoard';
import NotificationScreen from './NotificationScreen';

const Tab = createBottomTabNavigator({
    Home: {
        screen: DashBoard,
        navigationOptions: {
            tabBarLabel: 'Home',
            tabBarIcon: () => (
                <AntDesign name="home" size={30} color="black" />
            )
        }
    },
    NotificationScreen: {
        screen: NotificationScreen,
        navigationOptions: {
            tabBarLabel: 'Notifications',
            tabBarIcon: () => (
                <Ionicons name="notifications-sharp" size={30} color="black" />
            )
        }
    },
    More: {
        screen: NotificationScreen,
        navigationOptions: {
            tabBarLabel: 'More',
            tabBarIcon: () => (
                <MaterialIcons name="more" size={30} color="black" />
            )
        }
    }
});


export default Tab;