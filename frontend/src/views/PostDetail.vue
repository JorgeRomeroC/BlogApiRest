<template>
  <div class="realtive py-16 overflow-hidden">
      <div class="relative px-4 sm:px-6 lg:px-8">
        <div class="text-lg max-w-prose mx-auto">
          <h1>
            <span class="mt-2 block text-3x1 text-center leading-8 font-extrabold tracking-tight text-gray-900">{{$route.params.title}}</span>

          </h1>
          <p class="mt-8 text-x1 text-center leading-8">{{$route.params.excerpt}}</p>
        </div>
        <div class="mt-6 prose prose-indigo prose-lg text-gray-500 mx-auto">
            {{$route.params.content}}
        </div>
      </div>
  </div>
</template>
<script>
export default {

}
</script>