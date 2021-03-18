import axios from 'axios';
import AsyncStorage from '@react-native-community/async-storage';

const instance = axios.create({
    baseURL: 'http://192.168.5.3:8000'
});

// instance.interceptors.request.use(
//     async (config) => {
//         const token = JSON.parse(await AsyncStorage.getItem('token'));
//         if (token){
//             // const token = details.token;
//             config.headers.Authorization = `Bearer ${token}`;
//         }
//         return config;
//     },
//     (err) => {
//         return Promise.reject(err);
//     }
// );

export default instance;