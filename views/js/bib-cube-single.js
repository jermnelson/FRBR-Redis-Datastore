var WIDTH = 640;
var HEIGHT = 480;
var SPACER = 15;
var camera, scene, renderer, geometry, material, mesh;


function drawWEMIDemo() {
  $("#visualization").empty();
  var paper = Raphael("visualization",WIDTH,HEIGHT);
  var item_plane = paper.rect(75,140,270,190);
  item_plane.attr("stroke","#600");
  item_plane.attr("fill","#F3C73f");
  var manifestation_plane = paper.rect(95,120,270,190);
  manifestation_plane.attr("stroke","#0064CD");
  manifestation_plane.attr("fill","green");
  var expression_plane = paper.rect(115,100,270,190);
  expression_plane.attr("stroke","#0064CD");
  expression_plane.attr("fill","brown");
  var work_plane = paper.rect(135,80,270,190);
  work_plane.attr("stroke","#0064CD");
  work_plane.attr("fill","#049CDB");
  var work_label = paper.text(380,260,"frbr:Work");
  var expression_label = paper.text(340,280,"frbr:Expression");
  var manifestation_label = paper.text(320,300,"frbr:Manifestation");
  var item_label = paper.text(320,320,"frbr:Item");
  var mods_brane = paper.rect(75,140,270,190);
  mods_brane.attr("stroke","#000");
  mods_brane.rotate("-45",85,200);
} 

function animateWEMIDemo() {
 init();
 animiate();
}

function init() {
  scene = new THREE.Scene();
  camera = new THREE.PerspectiveCamera( 75, window.innerWidth / window.innerHeight, 1, 10000 );
  camera.position.z = 1000;
  scene.add( camera );

  geometry = new THREE.CubeGeometry( 200, 200, 200 );
  material = new THREE.MeshBasicMaterial( { color: 0xff0000, wireframe: true } );

  mesh = new THREE.Mesh( geometry, material );
  scene.add( mesh );

  renderer = new THREE.CanvasRenderer();
  renderer.setSize( window.innerWidth, window.innerHeight );

  document.body.appendChild( renderer.domElement );

}

function animate() {
// note: three.js includes requestAnimationFrame shim
 requestAnimationFrame( animate );
render();
}

function render() {
 mesh.rotation.x += 0.01;
 mesh.rotation.y += 0.02;
 renderer.render( scene, camera );
}

