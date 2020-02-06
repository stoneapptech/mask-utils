// https://www.post.gov.tw/post/internet/Postal/index.jsp?ID=208
var city = document.querySelector("#city");
var area = document.querySelector("#cityarea");
var result = {};
for (opt of city.children) {
  c_name = opt.value;
  if (c_name == "%") continue;
  console.log(c_name);
  city.value = c_name;
  citychange_23();
  result[c_name] = Array.from(area.children).map(e => {return e.innerText});
}
console.log(JSON.stringify(result, null, 2));