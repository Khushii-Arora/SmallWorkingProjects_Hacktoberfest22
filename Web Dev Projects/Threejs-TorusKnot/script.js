// The three.js scene: the 3D world where you put objects
const scene = new THREE.Scene();
const textureLoader = new THREE.TextureLoader();

// The camera
const camera = new THREE.PerspectiveCamera(
  45,
  window.innerWidth / window.innerHeight,
  1,
  1000
);
camera.position.z=3;
// camera.position.x= -1;
scene.add(camera)

// const texture = textureLoader.load('https://blenderartists.org/uploads/default/original/4X/b/d/3/bd375053de411c89435ec671c3e577f29d1f78a3.png')
const texture = textureLoader.load('./assets/matCap.png')

const geometry = new THREE.TorusKnotGeometry(0.5, 0.2, 200, 20)
const material = new THREE.MeshMatcapMaterial({matcap: texture})
const mesh = new THREE.Mesh(geometry, material)
scene.add(mesh)

const renderer = new THREE.WebGLRenderer({alpha: true});
renderer.setSize(window.innerWidth, window.innerHeight);
document.body.append(renderer.domElement);

const tick = () => {
  window.requestAnimationFrame(tick)
  mesh.rotation.y += 0.02
  renderer.render(scene, camera)
}
tick()

