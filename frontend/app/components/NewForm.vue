<template>
    <div>
        <div id="displayDiv">
            <h1 id="proj-name">{{ values[0].name}} </h1>
            <div id="github-div">
                 <div>
                    <h2 class="info-headers">GitHub URL</h2>
                </div>
                    <br>
                    <a :href="values[0].url">{{ values[0].url}}</a>
            </div>
             <div id="description-div">
                 <div>
                    <h2 class="info-headers">Project Description</h2>
                </div>
                    <br>
                    <p>{{ values[0].description}}</p>
            </div>
            <div>
                    <div>
                        <h2 class="info-headers">Languages Used:</h2>
                    </div>
                    <ul id="example-1">
                      <li v-for="languages in languages">
                        {{ languages.language }}
                      </li>
                    </ul>
                    <language-byte-bar-chart source="languageBytesUsed"
                       title="Bytes Used per Language "
                       cite-url=""
                       cite-text="Language Bytes">
                    </language-byte-bar-chart>
                    <div ref="holder" style="position: relative; z-index: 5">
                        <div class="chart">
                            <h3 style="text-align: center">{{ title }}</h3>
                            <vega-lite :spec="spec" :data="values"></vega-lite>
                            <p> {{ chart }} </p>
                        </div>
                    </div>
            </div>
            
            <input class="info-buttons" id="edit" type="button" @click="editMode" value="Edit">
            
        </div>
        <div id="editDiv" style="display:none;">

                <form action="" method="post">
                    <div>
                        <div>
                            <span>Project Name</span>
                        </div>
                        <input disabled type='text' :placeholder="values[0].name" id='name'>
                    </div>
                    <div>
                        <div>
                            <span>Project/ GitHub URL</span>
                        </div>
                        <input disabled id='url' type='text' :placeholder="values[0].url">
                    </div>

                    <div>
                        <span>Project Description:</span>
                    </div>
                    <textarea disabled id="description" form="projectForm" rows="2" cols="129">{{ values[0].description }}</textarea>
                    <br>
                
               

                <div id="buttonDiv" @click="makeLanguageList()">
                </div>
                <div id="buttonDiv">
                    
                    <input class="info-buttons" style="display:none;" id="cancel" type="button" @click="cancelInputs" value="Cancel">
                    <input class="info-buttons" style="display:none;" id="save" type="button" @click="saveInputs" value="Save">
                </div>
                <br>
                                
            </form>
        </div>
    
    </div>
</template>

<script type="text/javascript">

 import LanguageByteBarChart from './charts/LanguageByteBarChart'
 import { mapState } from 'vuex'
 import AugurStats from 'AugurStats'
  module.exports = {
    data() {
    
      return {
        values: [],
        languages: [],
        loaded: false,
        newLanguageText: ''
      }
    },
    components: {
        LanguageByteBarChart
    },
    methods: {
    
            editMode(){
            
                document.getElementById('description').disabled = false;
                document.getElementById('url').disabled = false;
                document.getElementById('name').disabled = false;
                
                var cancel = document.getElementById("cancel");
                cancel.style.display = "block";
                var save = document.getElementById("save");
                save.style.display = "block";
                
                var edit = document.getElementById("edit");
                edit.style.display = "none";
                
                var display = document.getElementById("displayDiv");
                display.style.display = "none";
                
                var editDiv = document.getElementById("editDiv");
                editDiv.style.display = "block";
                
                
            },
            
            cancelInputs(){
                
                var cancel = document.getElementById("cancel");
                cancel.style.display = "none";
                
                var save = document.getElementById("save");
                save.style.display = "none";
                
                var edit = document.getElementById("edit");
                edit.style.display = "block";
                
                var editDiv = document.getElementById("editDiv");
                editDiv.style.display = "none";
                
                var display = document.getElementById("displayDiv");
                display.style.display = "block";
            
            },
            
            saveInputs(){
            
                var project_name = document.getElementById("name").value;
                var github_url = document.getElementById("url").value;
                var project_description = document.getElementById("description").value;
                
                console.log('Project name: ' +project_name +' url: ' +github_url +' description: ' +project_description);
                
                 const url=('http://ec2-18-217-141-58.us-east-2.compute.amazonaws.com:5000/api/unstable/ghtorrent/edit_project_information?new_name='+project_name+'&new_description='+project_description+'&new_url='+github_url);
                console.log(url);
                const method={
                    method: "POST", 
                    mode: 'no-cors'
                 }
                 
                fetch(url, method)
                
            }
            

    },
    computed: {
        repo () {
            return this.$store.state.baseRepo
        },
        spec() {
           // IF YOU WANT TO CALL YOUR ENDPOINT IN THE CHART FILE, THIS IS WHERE/HOW YOU SHOULD DO IT:
         let repo = window.AugurAPI.Repo({ githubURL: this.repo })
         repo.languageBytesUsed().then((data) => {

           console.log("Language HERE", data)
           this.bytes = data
         })
         //FINISH CALLING ENDPOINT

         let config = {
           "$schema": "https://vega.github.io/schema/vega-lite/v2.json",
           "width": 950,
           "height": 300,
           "mark": "line",
           "encoding": {
             "x": {
               "field": "date", "type": "temporal",
             },
             "y": {
               "field": "value","type": "quantitative",
             },
           }
         }
         return config
       }
        
    },
    created(){
        let repo = window.AugurAPI.Repo({ githubURL: this.repo })
            repo.projectInformation().then((data) => {
            console.log("HERE", data)
            this.values = data
            
            })
            
        let language = window.AugurAPI.Repo({ githubURL: this.repo })
            language.getLanguages().then((data) => {
            console.log("TWO", data)
            this.languages = data
            
            })
    }
  }

</script>
