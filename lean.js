const axios = require('axios')
var fs = require('fs')

// insert twitter api keys and secrets here
const apiKey = process.env.TWITTER_API_KEY
const apiSecret = process.env.TWITTER_API_SECRET
const clientId = process.env.TWITTER_CLIENT_ID
const clientSecret = process.env.TWITTER_CLIENT_SECRET
const bearerToken = process.env.TWITTER_BEARER_TOKEN

const moriTwitterId = '1283653858510598144'
const kiaraTwitterId = '1283646922406760448'

let likedTweetsFromKiara = []

function timeout(ms) {
  return new Promise(resolve => setTimeout(resolve, ms))
}

// im retarded
const forLoop = async startPage => {
  let nextPage = startPage
  while (nextPage) {
    let url = `https://api.twitter.com/2/users/${moriTwitterId}/liked_tweets?expansions=author_id&pagination_token=${nextPage}`
    try {
      let res = await axios.get(url, {
        headers: {
          Authorization: `Bearer ${bearerToken}`
        }
      })

      // new v2 api rate limits way more so have to do this thanks elon
      await timeout(20000)

      const likedTweets = res.data.data
      likedTweetsFromKiara = [...likedTweetsFromKiara, ...likedTweets]
      console.log(likedTweetsFromKiara)
      console.log('\n\n')

      // get token next pagination
      nextPage = res.data.meta.next_token
    } catch (err) {
      console.log('\n\n')
      console.log('something in error', err.response.data)
      console.log(likedTweetsFromKiara)
    }
  }
}

axios
  .get(`https://api.twitter.com/2/users/${moriTwitterId}/liked_tweets?expansions=author_id`, {
    headers: {
      Authorization: `Bearer ${bearerToken}`
    }
  })
  .then(res => {
    const likedTweets = res.data.data
    likedTweetsFromKiara = [...likedTweetsFromKiara, ...likedTweets]
    console.log(likedTweetsFromKiara)
    let nextPage = res.data.meta.next_token
    console.log(likedTweetsFromKiara)
    console.log('\n\n')

    forLoop(nextPage).then(() => {
      console.log('\n\n')
      console.log(likedTweetsFromKiara)
      let text = likedTweetsFromKiara.map(x => JSON.stringify(x, null, 2)).join(',\n')
      fs.writeFileSync('likedTweets.txt', text, 'utf8')
    })
  })
  .catch(err => {
    console.log('\n\n')
    console.log('something in err', err.response.data)
    console.log(likedTweetsFromKiara)
  })
