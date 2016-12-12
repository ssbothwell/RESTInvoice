var json =
[
  {
    "id":1,
    "project_title": "Apollo 11",
    "client": "Gene Kranz",
    "lineitems": [
      {
        "id": 1,
        "name": "Solid Rocket",
        "description": "Big solid thruster",
        "price": "1000.00",
        "quantity": 2,
        "invoice": 1,
      },
      {
        "id": 2,
        "name": "GPS Unit",
        "description": "GPS Tracking Unit",
        "price": "3000.00",
        "quantity": 1,
        "invoice": 1
      }
    ]
  },
  {
    "id": 2,
    "project_title": "Infinite Improbability Drive",
    "client": "douglas adams",
    "lineitems": [],
  }
]


Vue.component('invoice-item', {
  delimiters: ['[[', ']]'], 
  props: ['invoice'],
  template: '#invoice-list-template'
})

var invoiceInstance = new Vue({
  el: '#invoiceList',
  data: {
    items: json
  },
})

