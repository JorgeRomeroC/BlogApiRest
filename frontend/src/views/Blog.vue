<template>
  <div class="bg-gray-100">
    <div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
      <div class="mx-auto max-w-2xl py-16 sm:py-24 lg:max-w-none lg:py-32">
        <h2 class="text-2xl font-bold text-gray-900">Collections</h2>

        <div class="mt-6 space-y-12 lg:grid lg:grid-cols-3 lg:gap-x-6 lg:space-y-0">
          <div v-for="posts in APIData" :key="posts.id" class="group relative">
            <div class="relative h-80 w-full overflow-hidden rounded-lg bg-white group-hover:opacity-75 sm:aspect-w-2 sm:aspect-h-1 sm:h-64 lg:aspect-w-1 lg:aspect-h-1">
              <img :src="{{ posts.thumbnail}}"  class="h-full w-full object-cover object-center" />
            </div>
            <h3 class="mt-6 text-sm text-gray-500">
              <router-link :to="{name:'BlogPost', params:{id:posts.id, title: posts.title, thumbnail: posts.thumbnail, slug: posts.slug, excerpt: posts.excerpt, content: posts.content}}">
                <span class="absolute inset-0" />
                {{ posts.title }}
              </router-link>
            </h3>
            <p class="text-base font-semibold text-gray-900">{{ posts.content }}</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import {getAPI} from "@/axios.api"

export default {
  name: 'Blog',
  data(){
    return{
      APIData: []
    }
  },
  created() {
    getAPI.get('/blog/posts/',)
        .then(response =>{
          console.log('Post API has recieved data')
          this.APIData = response.data
        })
        .catch(err => {
          console.log(err)
        })
  }
}
</script>
