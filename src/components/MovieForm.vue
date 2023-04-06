<template>
    <form @submit.prevent="saveMovie" id="movieForm">
        <div v-if="errors.length >0" class="alert alert-danger">
        <ul>
            <li v-for="error in errors" :key="error">{{ error }}</li>
        </ul>
        </div>
        <div v-if="successMessage" class="alert alert-success">
        {{ successMessage }}
        </div> 
      <div class="form-group mb-3">
        <label for="title" class="form-label">Movie Title</label>
        <input type="text" v-model="movieForm.title" name="title" class="form-control" />
      </div>
      <div class="form-group mb-3">
        <label for="poster" class="form-label">Movie Poster</label>
        <input type="file" @change="onFileChange" name="poster" class="form-control" />
      </div>
      <div class="form-group mb-3">
        <label for="description" class="form-label">Movie Description</label>
        <textarea v-model="movieForm.description" name="description" class="form-control"></textarea>
      </div>
      <button type="submit" class="btn btn-primary">Submit</button>
    </form>
</template>
  
<script setup>
  import { ref, onMounted } from 'vue';
  let csrf_token = ref("");
  let successMessage = ref("");
  let errors = ref([]);
  
  function getCsrfToken() {
  fetch('/api/v1/csrf-token')
  .then((response) => response.json())
  .then((data) => {
  console.log(data);
  csrf_token.value = data.csrf_token;
  })
  }

  onMounted(() => {
  getCsrfToken();
  });
  
  const movieForm = ref({
    title: '',
    poster: null,
    description: ''
  });
  
  const onFileChange = (event) => {
    movieForm.poster = event.target.files[0];
  };
  
  const saveMovie = () => {
    
    let movieForm = document.getElementById('movieForm');
    let form_data = new FormData(movieForm);
    fetch('/api/v1/movies', {
      method: 'POST',
      body: form_data,
      headers: {
        'X-CSRFToken': csrf_token.value
        }
    })
    .then(function (response) {
        return response.json();
    })
    .then(function (data) {
    // display a success message
        console.log(data);
    })
    .catch(function (error) {
        console.log(error);
    });
};
</script>