// components/screens/HomeScreen.js
import React from 'react';
import {
  View,
  FlatList,
  Image,
  Text,
  TouchableOpacity,
  StyleSheet,
  SafeAreaView,
} from 'react-native';

const icons = [
  { name: 'Kalender', image: require('../../assets/icons/3.png'), screen: 'Kalender' },
  { name: 'Lister', image: require('../../assets/icons/11.png'), screen: 'Lister' },
  { name: 'ADL', image: require('../../assets/icons/15.png'), screen: 'ADL' },
  { name: 'Små oppgaver', image: require('../../assets/icons/17.png'), screen: 'SmaOppgaver' },
  { name: 'Store oppgaver', image: require('../../assets/icons/16.png'), screen: 'StoreOppgaver' },
  { name: 'Fullført', image: require('../../assets/icons/20.png'), screen: 'Fullfort' },
];

export default function HomeScreen({ navigation }) {
  const renderItem = ({ item }) => (
    <View style={styles.iconContainer}>
      <TouchableOpacity
        style={styles.iconButton}
        onPress={() => navigation.navigate(item.screen)}
      >
        <Image source={item.image} style={styles.iconImage} />
      </TouchableOpacity>
      <Text style={styles.iconText}>{item.name}</Text>
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
    </SafeAreaView>
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
  },
  iconContainer: {
    alignItems: 'center',
    margin: 16,
  },
  iconButton: {
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
  iconImage: {
    width: '100%',
    height: '100%',
    resizeMode: 'cover',
  },
  iconText: {
    marginTop: 8,
    fontSize: 16,
    fontWeight: '600',
    color: '#333',
    textAlign: 'center',
  },
});
