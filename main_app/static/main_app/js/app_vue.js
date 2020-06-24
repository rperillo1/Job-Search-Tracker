function transformStr(str) {
    return str.replace(/\s/g, '+')
}
const jobTitle = document.getElementById('vue-search').innerText
const searchTerm = transformStr(jobTitle)
console.log(searchTerm)

const options = {
  url: 'https://jobs.github.com/positions.json?search=' + searchTerm +'&location=remote',
  method: 'GET',
  headers: {
    'Content-Type': 'application/json;charset=UTF-8',
  }}

const vueApp = new Vue({
    delimiters: ['${','}'],
    el: '#app',
    data () {
        return {
            info: null,
            loading: true,
            errored: false
        }
    },
    mounted () {
        axios(options)
        .then(response => {
            this.info = response.data.slice(0,5) 
        })
        .catch(error => {
            console.log(error)
            this.errored = true
        })
        .finally(() => this.loading = false)
    }
})