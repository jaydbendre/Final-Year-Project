import React from 'react';
import { StyleSheet, View, Modal, ViewPropTypes, BackHandler, Platform } from 'react-native';
import PropTypes from 'prop-types';
import LottieAnimation from 'lottie-react-native';

// For Navigation
import { withNavigation } from 'react-navigation';

class AnimatedLoader extends React.PureComponent {
  constructor(props){
    super(props);
  }

  static defaultProps = {
    visible: false,
    overlayColor: 'rgba(0, 0, 0, 0.25)',
    animationType: 'none',
    source: require('./loader.json'),
    animationStyle: {},
    speed: 1,
    loop: true,
    backButtonPress: () => Platform.OS === 'android' ? BackHandler.exitApp() : null,
  };

  static propTypes = {
    visible: PropTypes.bool,
    overlayColor: PropTypes.string,
    animationType: PropTypes.oneOf(['none', 'slide', 'fade']),
    source: PropTypes.object,
    animationStyle: ViewPropTypes.style,
    speed: PropTypes.number,
    loop: PropTypes.bool,
    backPress: PropTypes.func
  };

  animation = React.createRef();

  componentDidMount() {
    // console.log(this.props);
    if (this.animation.current) {
      this.animation.current.play();
    }
  }

  componentDidUpdate(prevProps) {
    const { visible } = this.props;
    if (visible !== prevProps.visible) {
      if (this.animation.current) {
        this.animation.current.play();
      }
    }
  }

  _renderLottie = () => {
    const { source, animationStyle, speed, loop } = this.props;
    return (
      <LottieAnimation
        ref={this.animation}
        source={source}
        loop={loop}
        speed={speed}
        style={[styles.animationStyle, animationStyle]}
      />
    );
  };

  render() {
    const { visible, overlayColor, animationType, backButtonPress } = this.props;

    return (
      <Modal
        transparent
        visible={visible}
        animationType={animationType}
        supportedOrientations={['portrait']}
        onRequestClose={backButtonPress}
      >
        <View style={[styles.container, { backgroundColor: overlayColor }]}>
          <View>{this._renderLottie()}</View>
        </View>
      </Modal>
    );
  }
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: 'transparent',
    position: 'absolute',
    top: 0,
    bottom: 0,
    left: 0,
    right: 0,
    alignItems: 'center',
    justifyContent: 'center',
  },
  animationStyle: {
    height: '100%',
    width: '100%',
  },
});


export default withNavigation(AnimatedLoader);
