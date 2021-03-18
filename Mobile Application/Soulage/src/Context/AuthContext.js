import { NativeModules } from 'react-native';
import createDataContext from './createDataContext';
import AsyncStorage from '@react-native-community/async-storage';

// For Navigation
import { navigate } from '../navigationRef';

// For API call
import SoulageApi from '../api/mainApi';

const { RNTwitterSignIn } = NativeModules;
// const TwitterCreds = {
//     "api_key": "hZO6gU344DJEi1mXKkJeDubci",
//     "secret_key": "FZ0WcumhDXaw6hkkQZRoqekIyVErcEaEYSBKcdeM2SoRU0hGqb"
// }

const TwitterCreds = {
    // "api_key": "hZO6gU344DJEi1mXKkJeDubci",
    // "secret_key": "FZ0WcumhDXaw6hkkQZRoqekIyVErcEaEYSBKcdeM2SoRU0hGqb",
    "api_key": "LTIzt6hjgpWjmSzkjx0i4hI1t",
    "secret_key": "sNGdak0JDGtE7PwBoiuXbRuDRvx0vj22mBtbXgwRnvHdiF09Ch",
    "access_token": "1066726122333896707-CsvLeX6O6sBIjBJ8JwZZ15ZSwJzQL8",
    "access_secret": "ZmcNqDQ80Kweu8ZxZgC1S9oT7irk9TzybcmjKA1ujuHHZ",
    "BEARER_TOKEN": "AAAAAAAAAAAAAAAAAAAAAGyWGgEAAAAAa44kQJAN294hEINsjN%2FdK84pKFU%3DES8eopWPj3IyNGf1sOOj3nTjFkdJplyLNkPRGQ0iKIF9Oqh97Z"
}


const authReducer = (state, actions) => {
    switch(actions.type){
        case 'error':
            return { errormsg: actions.payload }
        
        case 'signin':
            return { isSignedIn: true, token: actions.payload }
        
        case 'signout':
            return { isSignedIn: false, token: '' }
        
        default:
            return state
    }
}

const autoSignIn = (dispatch) => {
    return async () => {
        const token = JSON.parse(await AsyncStorage.getItem('token'));
        if(token){
            navigate('Dashboard');
        }else{
            navigate('LoginFlow');
        }
    }
}

const signIn = (dispatch) => {
    return async (username, password) => {
        data = {
            twitterusername: username,
            password
        }
        // console.log(data);
        try{
            const response = await SoulageApi.post('mobapp/login/', data);
            
            if(response.data.token){
                await AsyncStorage.setItem('token', response.data.token);
                dispatch({ type: 'signin', payload: response.data.token });
                navigate('Dashboard');
            }else {
                dispatch({ type: 'error', payload: response.data.msg });
                console.log(response.data.msg);
            }
        } catch (err){
            // console.log(err);
            // dispatch({ type: 'error', payload: 'Something went wrong...' });
            dispatch({ type: 'signin', payload: "response.data.token" });
            navigate('Dashboard');
        }
    }
}

const TwitterSignIn = (dispatch) => {
    return async () => {
        navigate('Loading');

        RNTwitterSignIn.init(TwitterCreds["api_key"], TwitterCreds["secret_key"]);
        RNTwitterSignIn.logIn().then(loginData => {
            // console.log(loginData);
            const { authToken, authTokenSecret } = loginData;
            if(authToken && authTokenSecret){
                console.log("Received Tokens Successfully...");
                navigate('Dashboard');

            }else {
                navigate('LoginFlow');
            }
        }).catch(err => {
            console.log(err);
            // navigate('LoginFlow');
        });

    }
}

const signOut = (dispatch) => {
    return async () => {
        try{
            await AsyncStorage.removeItem('token');
            dispatch({ type: 'signout' });
            navigate('LoginFlow');
        } catch(err){
            console.log(err);
            navigate('LoginFlow');
        }
    }
}

export const { Context, Provider } = createDataContext(
    authReducer,
    { autoSignIn, signIn, TwitterSignIn, signOut },
    { isSignedIn: false }
)