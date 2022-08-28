const EARTH_RADIUS_KM = 6371; // km
const SAT_SIZE = 100; // km
const TIME_STEP = 3 * 1000; // per frame

const timeLogger = document.getElementById('time-log');

const world = Globe()
  (document.getElementById('chart'))
  .globeImageUrl('//unpkg.com/three-globe@2.24.7/example/img/earth-blue-marble.jpg')
  .bumpImageUrl('//unpkg.com/three-globe/example/img/earth-topology.png')
  .objectLat('lat')
  .objectLng('lng')
  .objectAltitude('alt')
  .objectLabel('name');

setTimeout(() => world.pointOfView({ altitude: 2.5 }));

const satGeometry = new THREE.OctahedronGeometry(SAT_SIZE * world.getGlobeRadius() / EARTH_RADIUS_KM / 2, 0);
const satMaterial = new THREE.MeshLambertMaterial({ color: 'palegreen', transparent: true, opacity: 0.7 });
world.objectThreeObject(() => new THREE.Mesh(satGeometry, satMaterial));

fetch('https://raw.githubusercontent.com/vasturiano/globe.gl/master/example/datasets/space-track-leo.txt').then(r => r.text()).then(rawData => {
  const tleData = rawData.replace(/\r/g, '')
    .split(/\n(?=[^12])/)
    .filter(d => d)
    .map(tle => tle.split('\n'));
  const satData = tleData.map(([name, ...tle]) => ({
    satrec: satellite.twoline2satrec(...tle),
    name: name.trim().replace(/^0 /, '')
  }))
  // exclude those that can't be propagated
  .filter(d => !!satellite.propagate(d.satrec, new Date()).position)
  .slice(0, 2000);

  // time ticker
  let time = new Date();
  (function frameTicker() {
    requestAnimationFrame(frameTicker);

    time = new Date(+time + TIME_STEP);
    timeLogger.innerText = time.toString();

    // Update satellite positions
    const gmst = satellite.gstime(time);
    satData.forEach(d => {
      const eci = satellite.propagate(d.satrec, time);
      if (eci.position) {
        const gdPos = satellite.eciToGeodetic(eci.position, gmst);
        d.lat = satellite.radiansToDegrees(gdPos.latitude);
        d.lng = satellite.radiansToDegrees(gdPos.longitude);
        d.alt = gdPos.height / EARTH_RADIUS_KM
      }
    });

    world.objectsData(satData);
  })();
});