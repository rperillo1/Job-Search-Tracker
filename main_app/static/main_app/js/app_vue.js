function transformStr(str) {
  return str.replace(/\s/g, "+");
}
const jobTitle = document.getElementById("vue-search").innerText;
const searchTerm = transformStr(jobTitle);

const options = {
  url:
    "https://cors-anywhere.herokuapp.com/" +
    "https://jobs.github.com/positions.json?search=" +
    searchTerm +
    "&location=remote",
  method: "GET",
};

const vueApp = new Vue({
  delimiters: ["${", "}"],
  el: "#app",
  data() {
    return {
      info: null,
      loading: true,
      errored: false,
    };
  },
  mounted() {
    axios(options)
      .then((response) => {
        this.info = response.data.slice(0, 10);
      })
      .catch((error) => {
        console.log(error);
        this.errored = true;
      })
      .finally(() => (this.loading = false));
  },
});
