import React from 'react';
import { Text, View, StyleSheet } from 'react-native';

// For Charts and Graph
import {
    LineChart,
    BarChart,
    PieChart,
    ProgressChart,
    ContributionGraph,
    StackedBarChart
} from "react-native-chart-kit";

import { Dimensions } from "react-native";
const screenWidth = Dimensions.get("window").width;


const data = [
    {
        name: "sadness",
        percent: 50.0,
        color: "#808080",
        legendFontColor: "#7F7F7F",
        legendFontSize: 15
    },
    {
        name: "enthusiasm",
        percent: 1.0,
        color: "#FF8C00",
        legendFontColor: "#7F7F7F",
        legendFontSize: 15
    },
    {
        name: "neutral",
        percent: 1.0,
        color: "#FFFFE0",
        legendFontColor: "#7F7F7F",
        legendFontSize: 15
    },
    {
        name: "worry",
        percent: 25.0,
        color: "#FFFF00",
        legendFontColor: "#7F7F7F",
        legendFontSize: 15
    },
    {
        name: "surprise",
        percent: 3.0,
        color: "#4169E1",
        legendFontColor: "#7F7F7F",
        legendFontSize: 15
    },
    {
        name: "love",
        percent: 14.0,
        color: "#FF1493",
        legendFontColor: "#7F7F7F",
        legendFontSize: 15
    },
    {
        name: "fun",
        percent: 1.0,
        color: "#FF0000",
        legendFontColor: "#7F7F7F",
        legendFontSize: 15
    },
    {
        name: "hate",
        percent: 1.0,
        color: "#4B0082",
        legendFontColor: "#7F7F7F",
        legendFontSize: 15
    },
    {
        name: "boredom",
        percent: 3.0,
        color: "#696969",
        legendFontColor: "#7F7F7F",
        legendFontSize: 15
    },
    {
        name: "anger",
        percent: 1.0,
        color: "#800000",
        legendFontColor: "#7F7F7F",
        legendFontSize: 15
    }
];

const chartConfig = {
    backgroundGradientFrom: "#1E2923",
    backgroundGradientFromOpacity: 0,
    backgroundGradientTo: "#08130D",
    backgroundGradientToOpacity: 0.5,
    color: (opacity = 1) => `rgba(26, 255, 146, ${opacity})`,
    strokeWidth: 2, // optional, default 3
    barPercentage: 0.5,
    useShadowColorFromDataset: false // optional
};

const TweetSentiment = ({ sentiment }) => {
    return (
        <View style={styles.chart}>
            <PieChart
                data={sentiment}
                width={screenWidth}
                height={220}
                chartConfig={chartConfig}
                accessor="percent"
                backgroundColor="transparent"
                paddingLeft="15"
                absolute
            />
        </View>
    )
}

const styles = StyleSheet.create({
    chart: {
        justifyContent: 'center',
        alignItems: 'center'
    }
});

export default TweetSentiment;