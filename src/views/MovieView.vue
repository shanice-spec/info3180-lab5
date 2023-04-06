<template>
    <h2>Movies</h2>
    <div class="movie-cards">
      <div v-for="movie in movies" class="card">
        <div class="card-image">
          <img :src="movie.poster" alt="Movie poster" />
        </div>
        <div class="card-content">
          <h3>{{ movie.title }}</h3>
          <p>{{ movie.description }}</p>
        </div>
      </div>
    </div>
  </template>
  
  <style scoped>
    .movie-cards {
      display: flex;
      flex-wrap: wrap;
      justify-content: space-between;
    }
  
    .card {
      display: flex;
      flex-direction: row;
      background-color: #fff;
      box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
      border-radius: 0.5rem;
      overflow: hidden;
      width: 40%;
      margin-bottom: 1rem;
    }
  
    .card-image {
      flex: 0 0 40%;
      overflow: hidden;
    }
  
    .card-image img {
      width: 100%;
      height: 100%;
      object-fit: cover;
    }
  
    .card-content {
      flex: 1 1 auto;
      padding: 1rem;
    }
  
    .card-content h3 {
      margin-top: 0;
    }
  
    .card-content p {
      margin-bottom: 0;
    }
  </style>

<script setup>
    import { ref, onMounted } from "vue";
    let movies = ref([]);

    onMounted(() => {
    fetch('/api/v1/movies',{method:'GET'})
      .then((resp) => resp.json())
      .then((data) => {
        movies.value = data.movies
      })
      .catch((err) => console.log(err))
  })
</script>