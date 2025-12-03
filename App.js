// App.js
import React from 'react';
import { NavigationContainer } from '@react-navigation/native';
import { createNativeStackNavigator } from '@react-navigation/native-stack';
import { View, FlatList, Image, TouchableOpacity, Text, SafeAreaView, StyleSheet } from 'react-native';

import ADLScreen from './components/screens/ADLScreen';
import FullfortScreen from './components/screens/FullfortScreen';
import KalenderScreen from './components/screens/KalenderScreen';
import ListerScreen from './components/screens/ListerScreen';
import SmaOppgaverScreen from './components/screens/SmaOppgaverScreen';
import StoreOppgaverScreen from './components/screens/StoreOppgaverScreen';

const Stack = createNativeStackNavigator();

const icons = [
  { name: 'Kalender', image: require('./assets/icons/3.png'), screen: 'Kalender' },
  { name: 'Lister', image: require('./assets/icons/11.png'), screen: 'Lister' },
  { name: 'ADL', image: require('./assets/icons/15.png'), screen: 'ADL' },
  { name: 'Små oppgaver', image: require('./assets/icons/17.png'), screen: 'SmaOppgaver' },
  { name: 'Store oppgaver', image: require('./assets/icons/16.png'), screen: 'StoreOppgaver' },
  { name: 'Fullført', image: require('./assets/icons/20.png'), screen: 'Fullfort' },
];

function HomeScreen({ navigation }) {
  const renderItem = ({ item }) => (
    <View style={styles.iconContainer}>
      <TouchableOpacity
        style={styles.imageButton}
        onPress={() => navigation.navigate(item.screen)}>
        <Image source={item.image} style={styles.fullImage} />
      </TouchableOpacity>
      <Text style={styles.iconLabel}>{item.name}</Text>
    </View>
  );

  return (
    <SafeAreaView style={styles.container}>
      <FlatList
        data={icons}
        renderItem={renderItem}
        keyExtractor={(item, index) => index.toString()}
        numColumns={2}
        contentContainerStyle={styles.grid}
      />
      <View style={styles.bottomIcons}>
        <View style={styles.bottomIconContainer}>
          <TouchableOpacity style={styles.largeButton}>
            <Image source={require('./assets/icons/19.png')} style={styles.bottomImage} />
          </TouchableOpacity>
          <Text style={styles.iconLabel}>Logg ut</Text>
        </View>
        <View style={styles.bottomIconContainer}>
          <TouchableOpacity style={styles.largeButton}>
            <Image source={require('./assets/icons/7.png')} style={styles.bottomImage} />
          </TouchableOpacity>
          <Text style={styles.iconLabel}>Innstillinger</Text>
        </View>
      </View>
    </SafeAreaView>
  );
}

export default function App() {
  return (
    <NavigationContainer>
      <Stack.Navigator initialRouteName="Home" screenOptions={{ headerShown: false }}>
        <Stack.Screen name="Home" component={HomeScreen} />
        <Stack.Screen name="Kalender" component={KalenderScreen} />
        <Stack.Screen name="Lister" component={ListerScreen} />
        <Stack.Screen name="ADL" component={ADLScreen} />
        <Stack.Screen name="SmaOppgaver" component={SmaOppgaverScreen} />
        <Stack.Screen name="StoreOppgaver" component={StoreOppgaverScreen} />
        <Stack.Screen name="Fullfort" component={FullfortScreen} />
      </Stack.Navigator>
    </NavigationContainer>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fbe4d8',
    padding: 16,
  },
  grid: {
    alignItems: 'center',
    justifyContent: 'center',
    paddingBottom: 120,
  },
  iconContainer: {
    alignItems: 'center',
    margin: 16,
  },
  imageButton: {
    width: 140,
    height: 140,
    borderRadius: 32,
    overflow: 'hidden',
    backgroundColor: '#fff',
    justifyContent: 'center',
    alignItems: 'center',
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 4 },
    shadowOpacity: 0.2,
    shadowRadius: 6,
    elevation: 5,
  },
  fullImage: {
    width: '100%',
    height: '100%',
    resizeMode: 'cover',
  },
  iconLabel: {
    marginTop: 8,
    fontSize: 16,
    fontWeight: '600',
    color: '#333',
    textAlign: 'center',
  },
  bottomIcons: {
    flexDirection: 'row',
    justifyContent: 'space-around',
    paddingVertical: 16,
  },
  bottomIconContainer: {
    alignItems: 'center',
  },
  largeButton: {
    width: 100,
    height: 100,
    borderRadius: 24,
    backgroundColor: '#fff',
    justifyContent: 'center',
    alignItems: 'center',
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 4 },
    shadowOpacity: 0.2,
    shadowRadius: 6,
    elevation: 5,
  },
  bottomImage: {
    width: '100%',
    height: '100%',
    resizeMode: 'cover',
  },
});
