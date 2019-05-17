  <template>
     <div ref="holder" style="position: relative; z-index: 5">
       <div class="chart">
         <h3 style="text-align: center">{{ title }}</h3>
         <vega-lite :spec="spec" :data="values"></vega-lite>
         <p> {{ chart }} </p>
       </div>
     </div>
   </template>

<script> 
   import { mapState } from 'vuex'
   import AugurStats from 'AugurStats'
   
   export default {
     props: ['source', 'citeUrl', 'citeText', 'title', 'disableRollingAverage', 'alwaysByDate', 'data'],
     data() {
       return {
         values: [],
       }
     },
     created () {
     
           let bytes = window.AugurAPI.Repo({ githubURL: this.repo })
            bytes.languageBytesUsed().then((data) => {
            console.log("bytes", data)
            this.bytes = data
            
        })
     
     },
     computed: {
       repo() {
         return this.$store.state.baseRepo
       },
       spec() {
           // IF YOU WANT TO CALL YOUR ENDPOINT IN THE CHART FILE, THIS IS WHERE/HOW YOU SHOULD DO IT:
         let repo = window.AugurAPI.Repo({ githubURL: this.repo })
         repo.languageBytesUsed().then((data) => {

           console.log("New Language", data)
           this.values = data
         })

         // YOU CAN PLAY WITH SAMPLE SPEC OF A LINE CHART AT: 
         // https://vega.github.io/editor/#/examples/vega-lite/line
         // AND SEE THE DATA THAT THEY ARE USING AT:
         // https://vega.github.io/vega-lite/data/stocks.csv
         let config = {
             "$schema": "https://vega.github.io/schema/vega-lite/v3.json",
              "data": {
                "values": [
                  {"Language": "A","Number of Bytes": 28}, {"Language": "B","Number of Bytes": 55}, {"Language": "C","Number of Bytes": 43},
                  {"Language": "D","Number of Bytes": 91}, {"Language": "E","Number of Bytes": 81}, {"a": "F","Number of Bytes": 53},
                  {"Language": "G","Number of Bytes": 19}, {"Language": "H","Number of Bytes": 87}, {"Language": "I","Number of Bytes": 52}
                ]
              },
              "mark": "bar",
              "width": 950,
              "height": 300,
              "encoding": {
                "x": {"field": "Language", "type": "nominal"},
                "y": {"field": "Number of Bytes", "type": "quantitative"}
              }
         }
         return config
       }
     },
     methods: {
       //define any methods you may need here
       //you can call them anywhere with: this.methodName()
       
     }
   }
</script>
