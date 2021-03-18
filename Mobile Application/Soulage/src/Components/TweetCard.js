import React from 'react';
import { Text, View, StyleSheet, Image } from 'react-native';

const TweetCard = ({ image_uri, tweet_text }) => {
    return(
            <View style={styles.container}>
                <Image
                    style={styles.img}
                    source={{ uri: image_uri }}
                />
                <View style={styles.sideContainer}>
                    <Text>{tweet_text}</Text>
                </View>
            </View>
    )
}

TweetCard.defaultProps = {
    // image_uri: 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRmGjkRg52UnMD9w_yXPrco9NgZUDAxSEBfeA&usqp=CAU',
    image_uri: 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSI0vQFxiC3piD5u22-5KusNUaoQxc_4kXr_A&usqp=CAU',
    tweet_text: 'Georgia is not the only state that pushed through these last minute rules changes before the presidential election.” @marthamaccallum They forgot about our Constitution!'
}

const styles = StyleSheet.create({
    container: {
        flexDirection: 'row',
        justifyContent: 'flex-start',
        marginHorizontal: 20,
        alignContent: 'center',
        marginTop: 10,
    },
    sideContainer: {
        flex: 1,
        flexDirection: 'column',
        alignItems: 'flex-end',
        justifyContent: 'center',
        height: 150,
    },
    img: {
        width: 200,
        height: 180,
        marginRight: 20,
        borderRadius: 2
    }
});

export default TweetCard;