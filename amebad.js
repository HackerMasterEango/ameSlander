// Get all the videos of a channel so can search through all the videos and find something problematic!s

const axios = require('axios')
var fs = require('fs')

// channel you want to cancel
const YOUTUBE_CHANNEL_ID = 'UCyl1z3jo3XHR1riLFKG5UAg'

// have ur youtube api key here
const YOUTUBE_API_KEY = process.env.apiKey

const uploadsURL = `https://youtube.googleapis.com/youtube/v3/search?part=id%2Csnippet&channelId=${YOUTUBE_CHANNEL_ID}&type=video&maxResults=100&key=${YOUTUBE_API_KEY}`

let videoIds = []

// im dumb af
const forLoop = async startPage => {
  let nextPage = startPage
  for (let i = 0; i < 7; i++) {
    let url = `https://youtube.googleapis.com/youtube/v3/search?part=id%2Csnippet&channelId=${YOUTUBE_CHANNEL_ID}&pageToken=${nextPage}&type=video&maxResults=100&key=${YOUTUBE_API_KEY}`
    let res = await axios.get(url)
    nextPage = res.data.nextPageToken
    videoIds = [...videoIds, ...res.data.items.map(x => x.id.videoId)]
  }
}

axios.get(uploadsURL).then(res => {
  let nextPage = res.data.nextPageToken
  videoIds = [...videoIds, ...res.data.items.map(x => x.id.videoId)]

  forLoop(nextPage).then(() => {
    console.log(videoIds)

    let text = videoIds.map(x => `'${x}'`).join(',\n')
    fs.writeFileSync('videos.txt', text, 'utf8')
  })
})
