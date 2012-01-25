var WIDTH = 640;
var HEIGHT = 480;
var SPACER = 15;
var camera, scene, renderer, geometry, material, mesh;

var work_cube, expr_cube, manf_cube, item_cube, mods_plane;
var work_material, expr_material, manf_material, item_material;

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
  var mods_brane = paper.path("M175,300L175,50L80,110L80,140M80,330L80,340L175,300");
  var mods_label = paper.text(155,70,"MODS");
  var marc21_brane = paper.path("M200,305L200,50L175,65M120,330L120,340L200,305");
  var marc_label = paper.text(200,70,"MARC21");
  var dc_brane = paper.path("M235,305L235,50L200,70M155,330L155,340L235,305");
  var dc_label = paper.text(250,70,"Dublin Core");
//  var mods_brane = paper.rect(75,140,270,190);
//  mods_brane.attr("stroke","#000");
//  mods_brane.rotate("-45",85,200);
} 

function animateWEMIDemo() {
 init();
 animate()
}

function init() {
  var WIDTH = 400, HEIGHT = 300;
  var VIEW_ANGLE = 45, 
      ASPECT = WIDTH / HEIGHT,
      NEAR = 0.1,
      FAR = 10000;
      
  $("#visualization").empty();
  scene = new THREE.Scene();
  camera = new THREE.PerspectiveCamera( VIEW_ANGLE,
                                        ASPECT,
                                        NEAR,
                                        FAR);
  camera.position.z = 900;
  scene.add(camera);

  geometry = new THREE.CubeGeometry( 100, 50, 75 );
  material = new THREE.MeshBasicMaterial( { color: 0xff0000, wireframe: true } );

  mesh = new THREE.Mesh( geometry, material );
  //scene.add( mesh );
  
  
  work_material = new THREE.MeshBasicMaterial( { color: 0x0064CD, wireframe: true });
  work_cube = new THREE.Mesh( geometry, work_material);
  work_cube.position.x = -150;
  work_cube.position.z = 250;
  scene.add(work_cube);
  
  
  
  
  expr_material = new THREE.MeshBasicMaterial( { color: 0xa52a2a, wireframe: true } );
  expr_cube = new THREE.Mesh( geometry, expr_material );
  expr_cube.position.y = work_cube.position.y + 55;
  expr_cube.position.x = work_cube.position.x;
  expr_cube.position.z = 250;
  scene.add(expr_cube);
  
  manf_material = new THREE.MeshBasicMaterial( { color: 0x008000, wireframe: true } );
  manf_cube = new THREE.Mesh( geometry, manf_material);
  manf_cube.position.y = expr_cube.position.y + 55;
  manf_cube.position.x = expr_cube.position.x;
  manf_cube.position.z = 250;
  scene.add(manf_cube);
  
  item_material =  new THREE.MeshBasicMaterial( { color: 0xF3C73f, wireframe: true } );
  item_cube = new THREE.Mesh( geometry, item_material);
  item_cube.position.y = manf_cube.position.y + 55;
  item_cube.position.x = manf_cube.position.x;
  item_cube.position.z = 250;
  scene.add(item_cube);
  var plane_material = new THREE.MeshBasicMaterial( {color: 0xff0000, wireframe: true} );
  
  mods_plane = new THREE.Mesh( new THREE.PlaneGeometry( 200, 300, 4, 4), plane_material);
  mods_plane.overdraw = true;
  mods_plane.position.x = 100;
  mods_plane.position.y = 100;
  mods_plane.doubleSided = true;
  mods_plane.rotation.y = -180;
  scene.add(mods_plane);
  
  
   
  renderer = new THREE.CanvasRenderer();
  //renderer.setSize( window.innerWidth, window.innerHeight );
  renderer.setSize( 640, 480 );
  $("#visualization").append(renderer.domElement);

}

function animate() {
 requestAnimationFrame( animate );
 render();
}

function render() {
 work_cube.rotation.y = expr_cube.rotation.y = manf_cube.rotation.y = item_cube.rotation.y += 0.01;
 mods_plane.position.x -= .5;
 //mesh.rotation.x += 0.01;
 //mesh.rotation.y += 0.02;
 renderer.render( scene, camera );
}

