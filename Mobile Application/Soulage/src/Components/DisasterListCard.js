import React from 'react';
import { Text, View, StyleSheet, TouchableOpacity } from 'react-native';
import { navigate } from '../navigationRef';

const DisasterCard = ({ title }) => {
    return(
        <TouchableOpacity onPress={() => navigate('DisasterDescScreen', { id: title.id, name: title.name })}>
            <View style={styles.container}>
                <Text style={styles.text}>{title.name}</Text>
                <View style={styles.button}>
                    <Text style={styles.buttonText}>Donate</Text>
                </View>
            </View>
        </TouchableOpacity>
    )
}

DisasterCard.defaultProps = {
    title: {id: 1, name: 'Chennai Floods'}
}

const styles = StyleSheet.create({
    container: {
        flexDirection: 'row',
        justifyContent: 'space-between',
        elevation: 5,
        marginHorizontal: 10,
        marginVertical: 15,
        paddingVertical: 15,
        paddingHorizontal: 10,
        backgroundColor: '#FFFFFF',
    },
    text: {
        fontWeight: 'bold',
        fontSize: 20
    },
    button: {
        borderWidth: 1,
        borderRadius: 5,
        paddingHorizontal: 10,
        paddingVertical: 5,
        backgroundColor: 'blue',
    },
    buttonText: {
        color: 'white',
        textAlignVertical: 'center'
    }
});

export default DisasterCard;