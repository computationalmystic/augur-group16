<template>
    <div>
        <div id="displayDiv">
            <h1 id="proj-name">{{ values[0].name}} </h1>
            <div>
                 <div>
                    <span>GitHub URL</span>
                </div>
                    <a :href="values[0].url">GitHub</a>
            </div>
            <div>
                    <div>
                        <span>Languages Used:</span>
                    </div>
                    <ul id="example-1">
                      <li v-for="languages in languages">
                        {{ languages.language }}
                      </li>
                    </ul>
            </div>
             <div>
                 <div>
                    <span>Project Description</span>
                </div>
                    <p>{{ values[0].description}}</p>
            </div>
            <input id="edit" type="button" @click="editMode" value="Edit">
            
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
                    <button type='submit'>Save Project Information</button>
                </div>
                <div id="buttonDiv">
                    
                    <input style="display:none;" id="cancel" type="button" @click="cancelInputs" value="Cancel">
                    <input style="display:none;" id="save" type="button" @click="saveInputs" value="Save">
                </div>
                <br>
                                
            </form>
        </div>
    
    </div>
</template>

<script type="text/javascript">
  module.exports = {
    data() {
    
      return {
        values: [],
        languages: [],
        loaded: false,
        newLanguageText: ''
      }
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
