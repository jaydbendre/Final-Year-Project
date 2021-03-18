import React from 'react';
import { Text, View, StyleSheet, TouchableOpacity } from 'react-native';

// For Icons
import Feather from 'react-native-vector-icons/Feather';

import { withNavigation } from 'react-navigation';

const Header = ({ navigation, headerText, navOption }) => {
    if(navOption === true){
        return (
            <View style={styles.header}>
                <TouchableOpacity style={styles.sidemenu} onPress={() => navigation.openDrawer()}>
                    <Feather
                        name="menu"
                        size={30}
                    />
                </TouchableOpacity>
                <Text style={styles.headerText}>{headerText}</Text>
            </View>
        )
    }else {
        return (
            <View style={styles.header}> 
                {/* <TouchableOpacity style={styles.sidemenu} onPress={() => navigation.openDrawer()}>
                    <Feather
                        name="menu"
                        size={30}
                    />
                </TouchableOpacity> */}
                <Text style={styles.headerText1}>{headerText}</Text>
            </View>
        )
    }
}

Header.defaultProps = {
    headerText: 'Relevium',
    navOption: true
}

const styles = StyleSheet.create({
    header: {
        flex: 1,
        width: '100%',
        height: '100%',
        flexDirection: 'row',
        alignItems: 'center',
        justifyContent: 'center',
        width: '100%',
    },
    headerText: {
        fontWeight: 'bold',
        fontSize: 20,
        color: '#333',
        letterSpacing: 1,
        alignSelf: 'center',
        alignItems: 'center'
    },
    headerText1: {
        fontWeight: 'bold',
        fontSize: 20,
        color: '#333',
        letterSpacing: 1,
        alignSelf: 'center',
        alignItems: 'center',
        marginRight: '15%'
    },
    sidemenu: {
        position: 'absolute',
        left: '-1%'
    }
})

export default withNavigation(Header);