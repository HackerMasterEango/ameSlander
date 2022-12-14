// Get all the videos of a channel so can search through all the videos and find something problematic!s
const axios = require('axios')
var fs = require('fs')

// channel you want to cancel
const YOUTUBE_CHANNEL_ID = 'UCL_qhgtOy0dy1Agp8vkySQg'

// have ur youtube api key here
const YOUTUBE_API_KEY = process.env.YOUTUBE_API_KEY

// for lives add "&eventtype=live"
const uploadsURL = `https://youtube.googleapis.com/youtube/v3/search?part=id%2Csnippet&channelId=${YOUTUBE_CHANNEL_ID}&type=video&eventtype=live&maxResults=100&key=${YOUTUBE_API_KEY}`

let videoIds = []

// im dumb af
const forLoop = async startPage => {
  let nextPage = startPage
  while (nextPage) {
    let url = `https://youtube.googleapis.com/youtube/v3/search?part=id%2Csnippet&channelId=${YOUTUBE_CHANNEL_ID}&pageToken=${nextPage}&type=video&eventtype=live&maxResults=100&key=${YOUTUBE_API_KEY}`
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
