import React from 'react';
import { Text, View, StyleSheet } from 'react-native';

import LoginScreen from './screens/LoginScreen';

const IndexScreen = () => {
    return (
        // <View style={{ flex: 1 }}>
        //     <Text style={{ alignContent: 'center' }}>
        //         Home Screen
        //     </Text>
        // </View>
        <LoginScreen />
    )
}

const styles = StyleSheet.create({});

export default IndexScreen;