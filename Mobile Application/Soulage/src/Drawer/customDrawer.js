import React from 'react';
import { Text, View, StyleSheet } from 'react-native';

// For Icons
import Entypo from 'react-native-vector-icons/Entypo';
import AntDesign from 'react-native-vector-icons/AntDesign';
import Ionicons from 'react-native-vector-icons/Ionicons';
import Fontisto from 'react-native-vector-icons/Fontisto';
import Foundation from 'react-native-vector-icons/Foundation';
import Feather from 'react-native-vector-icons/Feather';
import FontAwesome5 from 'react-native-vector-icons/FontAwesome5';

// For Navigation
import { navigate } from '../navigationRef';

class CustomDrawer extends React.Component {
    constructor(props){
        super(props);
        this.items = [
            {
                navOptionIcon: '',
                navOptionName: 'Dashboard',
                navigateTo: 'Dashboard',
                iconFamily: 'Ionicons',
                iconName: 'md-home-outline'
            },
            {
                navOptionIcon: '',
                navOptionName: 'Donation',
                navigateTo: 'Disaster',
                iconFamily: 'FontAwesome5',
                iconName: 'donate'
            },
            {
                navOptionIcon: '',
                navOptionName: 'Profile',
                navigateTo: 'Profile',
                iconFamily: 'AntDesign',
                iconName: 'home'
            },
            {
                navOptionIcon: '',
                navOptionName: 'Notifications',
                navigateTo: 'Notification',
                iconFamily: 'Ionicons',
                iconName: 'notifications-outline'
            },
            {
                navOptionIcon: '',
                navOptionName: 'About Us',
                navigateTo: 'AboutUs',
                iconFamily: 'AntDesign',
                iconName: 'home'
            },
            {
                navOptionIcon: '',
                navOptionName: 'Terms & Conditions',
                navigateTo: 'TermsCondition',
                iconFamily: 'Foundation',
                iconName: 'clipboard-notes'
            },
            {
                navOptionIcon: '',
                navOptionName: 'Sign Out',
                navigateTo: 'SignOut',
                iconFamily: 'Feather',
                iconName: 'log-out'
            }
        ]
    }

    render(){
        return (
            <View style={styles.container}>
                <View style={{ marginBottom: '10%' }}>
                    <Entypo
                        name="user"
                        style={styles.profileIcon}
                    />
                </View>
                
                <View style={styles.divider}></View>

                <View style={styles.row}>
                    <View style={styles.icon}>
                        <Ionicons
                            name="md-home-outline"
                            size={30}
                        />
                    </View>
                    <Text style={styles.text} onPress={() => navigate('MainScreen')}>
                        {this.items[0].navOptionName}
                    </Text>
                </View>

                <View style={styles.row}>
                    <View style={styles.icon}>
                        <FontAwesome5
                            name="donate"
                            size={30}
                        />
                    </View>
                    <Text style={styles.text} onPress={() => navigate('DisasterListScreen')}>
                        {this.items[1].navOptionName}
                    </Text>
                </View>

                <View style={styles.row}>
                    <View style={styles.icon}>
                        <AntDesign
                            name="profile"
                            size={30}
                        />
                    </View>
                    <Text style={styles.text}>
                        {this.items[2].navOptionName}
                    </Text>
                </View>

                <View style={styles.row}>
                    <View style={styles.icon}>
                        <Ionicons
                            name="notifications-outline"
                            size={30}
                        />
                    </View>
                    <Text style={styles.text}>
                        {this.items[3].navOptionName}
                    </Text>
                </View>

                <View style={styles.row}>
                    <View style={styles.icon}>
                        <Fontisto
                            name="info"
                            size={30}
                        />
                    </View>
                    <Text style={styles.text}>
                        {this.items[4].navOptionName}
                    </Text>
                </View>

                <View style={styles.row}>
                    <View style={styles.icon}>
                        <Foundation
                            name="clipboard-notes"
                            size={30}
                        />
                    </View>
                    <Text style={styles.text}>
                        {this.items[5].navOptionName}
                    </Text>
                </View>

                <View style={styles.row}>
                    <View style={styles.icon}>
                        <Feather
                            name="log-out"
                            size={30}
                        />
                    </View>
                    <Text style={styles.text} onPress={() => navigate('LoginFlow')}>
                        {this.items[6].navOptionName}
                    </Text>
                </View>
            </View>
        )
    }
}

const styles = StyleSheet.create({
    container: {
        width: '100%',
        height: '100%',
        backgroundColor: '#fff',
        paddingTop: 20
    },
    profileIcon: {
        width: 150,
        height: 100,
        marginTop: 20,
        alignSelf: 'center',
        fontSize: 90
    },
    divider: {
        width: '100%',
        height: 1,
        backgroundColor: '#e2e2e2',
        marginVertical: 30,
    },
    row: {
        flexDirection: 'row',
        alignItems: 'flex-start',
        paddingTop: 10,
        paddingBottom: 10,
        marginVertical: '2%'
    },
    icon: {
        marginRight: 15,
        marginLeft: 10
    },
    text: {
        fontSize: 15,
        textAlign: 'left',
        textAlignVertical: 'center',
        paddingTop: 12,
        position: "absolute",
        left: '25%'
    }
})

export default CustomDrawer;