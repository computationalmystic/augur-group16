<template>
    <div>
        <p>Print to the page</p>
        <p>New Headers</p>
        <form action="/handleNewForm" method="post">
                                <div>
                                    <div>
                                        <span>Project Name</span>
                                    </div>
                                    <input type='text' placeholder='Name' id='name' name='name'>
                                </div>
                                <div>
                                    <div>
                                        <span>Goal 1</span>
                                    </div>
                                    <input type='text' placeholder='Goal 1' name='goal1'>
                                </div>
                                 <div>
                                    <div>
                                        <span>Goal 2</span>
                                    </div>
                                    <input type='text' placeholder='Goal 2' name='goal2'>
                                </div>
                                 <div>
                                    <div>
                                        <span>Goal 3</span>
                                    </div>
                                    <input type='text' placeholder='Goal 3' name='goal3'>
                                </div>
                                <div>
                                    <div>
                                        <span>Project/ GitHub URL</span>
                                    </div>
                                    <input type='text' placeholder='URL' name='url'>
                                </div>
                               
                                
                                <textarea name="projectDescription" form="projectForm" rows="4" cols="129">Enter Project Description here...</textarea>
                                <br>

                                
                                <div id="buttonDiv">
                                    <button type='submit' name='submit'>Save Project Information</button>
                                </div>
                                <br>
                                
                            </form>
    </div>
</template>

<script>
  module.exports = {
    data() {
      return {

      }
    },
    methods: {

    },
    computed: {

    }
  }

</script>
