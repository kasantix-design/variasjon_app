// App.js
import React from 'react';
import { NavigationContainer } from '@react-navigation/native';
import { createNativeStackNavigator } from '@react-navigation/native-stack';
import HomeScreen from './components/screens/HomeScreen';
import KalenderScreen from './components/screens/KalenderScreen';
import ListerScreen from './components/screens/ListerScreen';
import ADLScreen from './components/screens/ADLScreen';
import SmaOppgaverScreen from './components/screens/SmaOppgaverScreen';
import StoreOppgaverScreen from './components/screens/StoreOppgaverScreen';
import FullfortScreen from './components/screens/FullfortScreen';

const Stack = createNativeStackNavigator();

export default function App() {
  return (
    <NavigationContainer>
      <Stack.Navigator screenOptions={{ headerShown: false }}>
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
