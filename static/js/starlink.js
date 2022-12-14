const EARTH_RADIUS_KM = 6371; // km
const SAT_SIZE = 100; // km
const TIME_STEP = 3 * 500; // per frame

const timeLogger = document.getElementById('time-log');

const world = Globe()
  (document.getElementById('chart'))
  .globeImageUrl('/static/imgs/earth-blue-marble.webp')
  .bumpImageUrl('/static/imgs/earth-topology.webp')
  .backgroundImageUrl('/static/imgs/nightsky.webp')
  .objectLat('lat')
  .objectLng('lng')
  .objectAltitude('alt')
  .objectLabel('name');

setTimeout(() => world.pointOfView({ altitude: 2.5 }));

const satGeometry = new THREE.OctahedronGeometry(SAT_SIZE * world.getGlobeRadius() / EARTH_RADIUS_KM / 2, 0);
const satMaterial = new THREE.MeshLambertMaterial({ color: 'palegreen', transparent: true, opacity: 0.7 });
world.objectThreeObject(() => new THREE.Mesh(satGeometry, satMaterial));

// Add globe rotation
world.controls().autoRotate = true;
world.controls().autoRotateSpeed = 0.35;

// Set clouds settings
const CLOUDS_IMG_URL = '/static/imgs/fair-clouds.webp';
const CLOUDS_ALT = 0.004;
const CLOUDS_ROTATION_SPEED = -0.006; // deg/frame

// Load cloud texture
new THREE.TextureLoader().load(CLOUDS_IMG_URL, cloudsTexture => {
  const clouds = new THREE.Mesh(
    new THREE.SphereBufferGeometry(world.getGlobeRadius() * (1 + CLOUDS_ALT), 75, 75),
    new THREE.MeshPhongMaterial({ map: cloudsTexture, transparent: true })
  );
  world.scene().add(clouds);

  (function rotateClouds() {
    clouds.rotation.y += CLOUDS_ROTATION_SPEED * Math.PI / 180;
    requestAnimationFrame(rotateClouds);
  })();
});


// Main fetch function
// TLE data is stored in a dedicated view/url that serves a raw txt file
fetch('../starlink_txt/', { cache: "force-cache" }).then(r => r.text()).then(rawData => {
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