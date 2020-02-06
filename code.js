// https://bthr.gov.taipei/News_Content.aspx?n=A75E2BF58F8BC883&s=A0B263D2B83B811B
var t = document.querySelector("tbody");
var c = {};
Array.from(t.children).forEach((e, _i)=>{
  name = e.children[0].innerText.trim();
  code = e.children[1].innerText.trim();
  console.log(name.slice(0,3), code)
  c[name.slice(0,3)] = code;
});
console.log(JSON.stringify(c, null, 2));