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

// const texture = textureLoader.load('https://bruno-simon.com/prismic/matcaps/8.png')
// const texture = textureLoader.load('https://blenderartists.org/uploads/default/original/4X/b/d/3/bd375053de411c89435ec671c3e577f29d1f78a3.png')
const texture = textureLoader.load('./assets/matCap.png')
// const texture = textureLoader.load('https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/d2ea35bd-7075-4131-a488-2e5a8583aeaf/db1k233-adc8c64e-f3e3-470d-b1f5-708b2bffa3f3.png/v1/fill/w_350,h_350,strp/matcap__6_by_kurich_db1k233-350t.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9NTEyIiwicGF0aCI6IlwvZlwvZDJlYTM1YmQtNzA3NS00MTMxLWE0ODgtMmU1YTg1ODNhZWFmXC9kYjFrMjMzLWFkYzhjNjRlLWYzZTMtNDcwZC1iMWY1LTcwOGIyYmZmYTNmMy5wbmciLCJ3aWR0aCI6Ijw9NTEyIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmltYWdlLm9wZXJhdGlvbnMiXX0.98SdtFzmhkcNbDAYSDA9oOUgto-nu_rhIW9Rc28xhic')
// const texture = textureLoader.load('http://mua.github.io/models/matcap/JGSpecial_01.png')

const geometry = new THREE.TorusKnotGeometry(0.5, 0.2, 200, 20)
const material = new THREE.MeshMatcapMaterial({matcap: texture})
const mesh = new THREE.Mesh(geometry, material)
scene.add(mesh)

const renderer = new THREE.WebGLRenderer({alpha: true});
renderer.setSize(window.innerWidth, window.innerHeight);
document.body.append(renderer.domElement);

// var controls = new OrbitControls(camera, renderer.domElement);

const tick = () => {
  window.requestAnimationFrame(tick)
  mesh.rotation.y += 0.02
  renderer.render(scene, camera)
}
tick()

