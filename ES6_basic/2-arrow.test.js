import getNeighborhoodsList from './2-arrow'; // Importez la fonction à tester

// Cas de test pour la fonction getNeighborhoodsList
describe('getNeighborhoodsList', () => {
  let neighborhoodsList;

  // Avant chaque test, initialisez une nouvelle instance de getNeighborhoodsList
  beforeEach(() => {
    neighborhoodsList = new getNeighborhoodsList();
  });

  test('addNeighborhood should add a new neighborhood to the list', () => {
    const res = neighborhoodsList.addNeighborhood('Noe Valley');
    expect(res).toEqual(['SOMA', 'Union Square', 'Noe Valley']);
  });

  test('addNeighborhood should return the updated list of neighborhoods', () => {
    neighborhoodsList.addNeighborhood('Noe Valley');
    const res = neighborhoodsList.addNeighborhood('Mission District');
    expect(res).toEqual(['SOMA', 'Union Square', 'Noe Valley', 'Mission District']);
  });
});
