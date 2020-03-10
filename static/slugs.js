const titleInput = document.querySelector("input[name=title]");
const slugInput = document.querySelector("input[name=slug]");


const titleToSlug = (val) => {
  return val.toString()
    .toLowerCase()
    .trim()
    .replace(/&/g,'-and-')
    .replace(/[\s\W-]+/g, '-') //replaces spaces, special characters with single dash
}

titleInput.addEventListener('keyup', (e) => {
  slugInput.setAttribute('value', titleToSlug(titleInput.value));
})