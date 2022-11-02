<template>
  <div class="border">
    <h1>This in hyejin's component</h1>
    <!-- 3. 보여주기 -->
    <MyComponentItem 
    static-props="MyComponent에서 보낸 데이터"
    :dynamic-props="dynamicProps"
    @look-at-me="parentGetEvent"
    @child-input="getDynamicData"/>
  </div>
</template>

<script>
// 1. 불러오기
import MyComponentItem from '@/components/MyComponentItem'

export default {
  name: 'MyComponent',

  components: {
    // 2. 등록하기
    MyComponentItem,
  },

  data: function () {
    return {
      dynamicProps: "It's in data"
    }
  },

  methods: {
    parentGetEvent (childData) {
      console.log('why??')
      console.log(childData)
    },

    getDynamicData (childInputData) {
      console.log(`사용자가 입력한 값은 ${childInputData}입니다.`)
    }
  }
}
</script>

<style>
  .border {
    border: solid 1px black;
  }
</style>