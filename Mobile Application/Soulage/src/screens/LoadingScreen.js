import React from 'react';
// import { View, Text } from 'react-native';

import AnimatedLoader from '../Spinner/spinner';

const LoadingScreen = () => {
    return (
        <AnimatedLoader
            visible={true}
            source={require('../Spinner/loader.json')}
            overlayColor="rgba(255,255,255,0.75)"
            animationStyle={{ width: '100%', height: '100%' }}
            speed={1}
        />
    )
}

export default LoadingScreen;