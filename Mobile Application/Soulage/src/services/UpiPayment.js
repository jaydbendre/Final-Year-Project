import RNUpiPayment from 'react-native-upi-payment';

export default ({ amount, onPayment }) => {
    console.log("From UPI Payment: ", amount);
    const successCallback = (data) => {
        console.log(data);
        onPayment(data);
    }

    const failureCallback = (data) => {
        console.log(data);
        onPayment(data);
    }

    RNUpiPayment.initializePayment({
        vpa: 'vickypillai19@oksbi',
        payeeName: 'Vignesh',
        amount: amount,
        transactionRef: 'aasf-332-aoei-fn',
        transactionNote: 'Upi Testing',
    }, successCallback, failureCallback);
}