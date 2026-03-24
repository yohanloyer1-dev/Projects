# Remotion Best Practices

Use this skill whenever you are dealing with Remotion code to obtain domain-specific knowledge for creating videos programmatically with React.

**Tags:** remotion, video, react, animation, composition, typescript

---

## Core Concepts

### Video Fundamentals
A video in Remotion is "a function of images over time." Every video requires:
- **width/height**: Pixel dimensions
- **durationInFrames**: Total frame count
- **fps**: Frames per second (playback speed)

Frame numbering is zero-indexed: first frame is `0`, last frame is `durationInFrames - 1`.

### Essential Hooks

```tsx
import { useCurrentFrame, useVideoConfig } from 'remotion';

const MyComponent = () => {
  const frame = useCurrentFrame(); // Current frame number (0-indexed)
  const { width, height, fps, durationInFrames, id } = useVideoConfig();

  return <div>Frame: {frame}</div>;
};
```

**Note:** Inside a `<Sequence>`, `useCurrentFrame()` returns the frame relative to when the Sequence starts, not the absolute timeline position.

---

## Animation Rules

### CRITICAL: Animation Requirements

**ALL animations MUST be driven by `useCurrentFrame()`.**

```tsx
// CORRECT: Frame-based animation
const frame = useCurrentFrame();
const { fps } = useVideoConfig();
const opacity = interpolate(frame, [0, fps * 2], [0, 1], {
  extrapolateRight: 'clamp',
});

// FORBIDDEN: CSS transitions/animations - they won't render properly
// FORBIDDEN: Tailwind animate-* or transition-* classes
// FORBIDDEN: useFrame() from React Three Fiber
```

### interpolate() Function

Maps values from one range to another:

```tsx
import { interpolate, Easing } from 'remotion';

const opacity = interpolate(
  frame,              // Input value
  [0, 30],           // Input range
  [0, 1],            // Output range
  {
    extrapolateLeft: 'clamp',   // 'extend' | 'clamp' | 'wrap' | 'identity'
    extrapolateRight: 'clamp',
    easing: Easing.out(Easing.cubic),
  }
);
```

### spring() Animation

Physics-based spring animations:

```tsx
import { spring } from 'remotion';

const scale = spring({
  frame,
  fps,
  from: 0,
  to: 1,
  config: {
    mass: 1,
    damping: 10,      // Higher = less bounce
    stiffness: 100,   // Higher = more bouncy
    overshootClamping: false,
  },
  durationInFrames: 60,  // Optional: stretch animation
  delay: 10,             // Optional: delay start
});
```

### Available Easing Functions

```tsx
import { Easing } from 'remotion';

// Predefined curves
Easing.linear
Easing.ease
Easing.quad
Easing.cubic
Easing.poly(n)    // Power function
Easing.sin
Easing.circle
Easing.exp
Easing.elastic
Easing.back
Easing.bounce
Easing.bezier(x1, y1, x2, y2)

// Modifiers
Easing.in(easing)
Easing.out(easing)
Easing.inOut(easing)
```

---

## Components

### Composition

Registers a video for rendering:

```tsx
// src/Root.tsx
import { Composition } from 'remotion';
import { MyVideo } from './MyVideo';

export const RemotionRoot = () => {
  return (
    <Composition
      id="my-video"
      component={MyVideo}
      durationInFrames={300}
      fps={30}
      width={1920}
      height={1080}
      defaultProps={{
        title: "Hello World",
      }}
      // Optional: dynamic metadata
      calculateMetadata={async ({ props }) => {
        return {
          durationInFrames: 600,
          props: { ...props, data: await fetchData() },
        };
      }}
    />
  );
};
```

### AbsoluteFill

Full-screen overlay container for layering:

```tsx
import { AbsoluteFill } from 'remotion';

// Later elements render on top
<AbsoluteFill>
  <Video src={staticFile('bg.mp4')} />
</AbsoluteFill>
<AbsoluteFill>
  <h1>Overlay Text</h1>
</AbsoluteFill>
```

### Sequence

Controls timing of when elements appear:

```tsx
import { Sequence } from 'remotion';

<Sequence from={30} durationInFrames={60} name="Title">
  <Title />  {/* Appears at frame 30, lasts 60 frames */}
</Sequence>

// Trim content from start (skip first 15 frames)
<Sequence from={0}>
  <Sequence from={-15}>
    <Animation />
  </Sequence>
</Sequence>
```

**Props:**
- `from`: Start frame (default: 0)
- `durationInFrames`: Duration (default: Infinity)
- `layout`: `"absolute-fill"` (default) or `"none"`
- `premountFor`: Premount N frames before display
- `name`: Label in Studio timeline

### Series

Sequential playback of scenes:

```tsx
import { Series } from 'remotion';

<Series>
  <Series.Sequence durationInFrames={60}>
    <Intro />
  </Series.Sequence>
  <Series.Sequence durationInFrames={120} offset={-10}>
    {/* Overlaps previous by 10 frames */}
    <MainContent />
  </Series.Sequence>
  <Series.Sequence durationInFrames={60}>
    <Outro />
  </Series.Sequence>
</Series>
```

### TransitionSeries

Animated transitions between scenes:

```tsx
import { TransitionSeries } from '@remotion/transitions';
import { fade } from '@remotion/transitions/fade';
import { slide } from '@remotion/transitions/slide';
import { linearTiming, springTiming } from '@remotion/transitions';

<TransitionSeries>
  <TransitionSeries.Sequence durationInFrames={60}>
    <Scene1 />
  </TransitionSeries.Sequence>
  <TransitionSeries.Transition
    presentation={fade()}
    timing={linearTiming({ durationInFrames: 30 })}
  />
  <TransitionSeries.Sequence durationInFrames={60}>
    <Scene2 />
  </TransitionSeries.Sequence>
  <TransitionSeries.Transition
    presentation={slide({ direction: 'from-right' })}
    timing={springTiming({ config: { damping: 200 } })}
  />
  <TransitionSeries.Sequence durationInFrames={60}>
    <Scene3 />
  </TransitionSeries.Sequence>
</TransitionSeries>
```

**Available transitions:** `fade`, `slide`, `wipe`, `flip`, `clockWipe`
**Slide directions:** `"from-left"`, `"from-right"`, `"from-top"`, `"from-bottom"`

**Duration calculation:** Total = sum of sequences - sum of transitions

---

## Media Components

### Images

Always use `<Img>` component to prevent flickering:

```tsx
import { Img, staticFile } from 'remotion';

// Local image (in public/ folder)
<Img src={staticFile('image.png')} style={{ width: 200 }} />

// Remote image (CORS required)
<Img src="https://example.com/image.jpg" />

// Dynamic paths
<Img src={staticFile(`frame-${frame}.png`)} />
```

**Never use:** Native `<img>`, Next.js `<Image>`, CSS `background-image`

### Video

```tsx
import { Video } from '@remotion/media';
// or for player compatibility:
import { OffthreadVideo } from 'remotion';

<Video
  src={staticFile('clip.mp4')}
  volume={0.5}                    // 0-1 or callback function
  playbackRate={1.5}              // Speed multiplier
  muted={false}
  trimBefore={30}                 // Skip first 30 frames
  trimAfter={150}                 // End at frame 150
  loop={true}
/>
```

**OffthreadVideo** is preferred for rendering (better performance, more codec support).

### Audio

```tsx
import { Audio } from '@remotion/media';

<Audio
  src={staticFile('music.mp3')}
  volume={(frame) => interpolate(frame, [0, 30], [0, 1])}  // Fade in
  playbackRate={1}
  muted={false}
  loop={true}
  trimBefore={0}
  trimAfter={300}
  toneFrequency={1}  // Pitch adjustment (0.01-2), render only
/>

// Delay audio start
<Sequence from={60}>
  <Audio src={staticFile('sound.mp3')} />
</Sequence>
```

### GIFs

```tsx
import { Gif } from '@remotion/gif';
// or for APNG/AVIF/WebP:
import { AnimatedImage } from 'remotion';

<Gif
  src={staticFile('animation.gif')}
  width={400}
  height={400}
  fit="contain"           // 'fill' | 'contain' | 'cover'
  playbackRate={1}
  loopBehavior="loop"     // 'loop' | 'pause-after-finish' | 'unmount-after-finish'
/>
```

### Lottie Animations

```tsx
import { Lottie } from '@remotion/lottie';
import { delayRender, continueRender } from 'remotion';

const [handle] = useState(() => delayRender());
const [animationData, setAnimationData] = useState(null);

useEffect(() => {
  fetch(staticFile('animation.json'))
    .then((res) => res.json())
    .then((data) => {
      setAnimationData(data);
      continueRender(handle);
    });
}, []);

{animationData && (
  <Lottie animationData={animationData} style={{ width: 400 }} />
)}
```

---

## Assets & Fonts

### Static Files

Place files in `public/` folder, reference with `staticFile()`:

```tsx
import { staticFile } from 'remotion';

const imageUrl = staticFile('images/photo.png');
const videoUrl = staticFile('videos/clip.mp4');
```

### Google Fonts

```tsx
import { loadFont } from '@remotion/google-fonts/Lobster';

const { fontFamily } = loadFont({
  weights: ['400', '700'],
  subsets: ['latin'],
});

// Use in styles
<div style={{ fontFamily }}>Text</div>
```

### Local Fonts

```tsx
import { loadFont } from '@remotion/fonts';
import { staticFile } from 'remotion';

loadFont({
  family: 'MyFont',
  url: staticFile('fonts/MyFont.woff2'),
  weight: '400',
});
```

---

## 3D Content (React Three Fiber)

```tsx
import { ThreeCanvas } from '@remotion/three';
import { useCurrentFrame } from 'remotion';

const My3DScene = () => {
  const frame = useCurrentFrame();
  const rotation = frame * 0.02;

  return (
    <ThreeCanvas width={1920} height={1080}>
      <ambientLight intensity={0.5} />
      <pointLight position={[10, 10, 10]} />
      <mesh rotation={[0, rotation, 0]}>
        <boxGeometry args={[1, 1, 1]} />
        <meshStandardMaterial color="orange" />
      </mesh>
    </ThreeCanvas>
  );
};
```

**Critical Rules:**
- Use `<ThreeCanvas>` with `width` and `height` props
- Animate with `useCurrentFrame()`, NOT `useFrame()` from R3F
- Add `layout="none"` to any `<Sequence>` inside ThreeCanvas
- Include lighting components

---

## Captions & Subtitles

```tsx
import { createTikTokStyleCaptions } from '@remotion/captions';

const { pages } = createTikTokStyleCaptions({
  captions,
  combineTokensWithinMilliseconds: 1200,
});

{pages.map((page, i) => (
  <Sequence
    key={i}
    from={Math.floor((page.startMs / 1000) * fps)}
    durationInFrames={Math.ceil(((page.endMs - page.startMs) / 1000) * fps)}
  >
    <CaptionDisplay page={page} />
  </Sequence>
))}
```

---

## Data Visualization

### Animated Bar Chart

```tsx
const STAGGER_DELAY = 5;

{data.map((item, i) => {
  const progress = spring({
    frame: frame - i * STAGGER_DELAY,
    fps,
    config: { damping: 200 },
  });
  return (
    <div
      key={i}
      style={{ height: item.value * progress }}
    />
  );
})}
```

**Critical:** Disable all animations from third-party charting libraries - they cause flickering.

---

## Text Measurement

```tsx
import { measureText, fitText, fillTextBox } from '@remotion/layout-utils';

// Measure text dimensions
const { width, height } = measureText({
  text: "Hello",
  fontFamily: "Arial",
  fontSize: 32,
});

// Fit text to container width
const { fontSize } = fitText({
  text: "Hello World",
  withinWidth: 600,
  fontFamily: "Inter",
});

// Detect text overflow
const box = fillTextBox({ maxBoxWidth: 400, maxLines: 3 });
words.forEach(word => {
  const { exceedsBox } = box.add({ text: word, fontFamily: "Arial", fontSize: 24 });
});
```

---

## DOM Measurement

Account for Remotion's scale transform:

```tsx
import { useCurrentScale } from 'remotion';

const scale = useCurrentScale();
const ref = useRef<HTMLDivElement>(null);

useEffect(() => {
  if (ref.current) {
    const rect = ref.current.getBoundingClientRect();
    const actualWidth = rect.width / scale;
    const actualHeight = rect.height / scale;
  }
}, [scale]);
```

---

## Dynamic Metadata (calculateMetadata)

```tsx
import { getMediaMetadata } from '@remotion/media-utils';

<Composition
  id="dynamic-video"
  component={MyVideo}
  durationInFrames={1}  // Placeholder
  fps={30}
  width={1920}
  height={1080}
  calculateMetadata={async ({ props, abortSignal }) => {
    const metadata = await getMediaMetadata(props.videoUrl, { signal: abortSignal });
    return {
      durationInFrames: Math.ceil(metadata.durationInSeconds * 30),
      width: metadata.width,
      height: metadata.height,
      props: { ...props, duration: metadata.durationInSeconds },
    };
  }}
/>
```

---

## Rendering

### Programmatic Rendering

```tsx
import { renderMedia, selectComposition, bundle } from '@remotion/renderer';

const bundled = await bundle({ entryPoint: './src/index.ts' });
const composition = await selectComposition({ serveUrl: bundled, id: 'my-video' });

await renderMedia({
  composition,
  serveUrl: bundled,
  codec: 'h264',  // h264, h265, vp8, vp9, prores, gif
  outputLocation: 'out/video.mp4',
  inputProps: { title: 'My Video' },
  onProgress: ({ progress }) => console.log(`${Math.round(progress * 100)}%`),
});
```

---

## TailwindCSS

TailwindCSS is fully supported in Remotion projects.

**Allowed:** All utility classes for styling
**Forbidden:** `transition-*` and `animate-*` classes (use `useCurrentFrame()` instead)

---

## Text Animations

### Typewriter Effect

Use string slicing, never per-character opacity:

```tsx
const frame = useCurrentFrame();
const { fps } = useVideoConfig();
const text = "Hello World";
const charsPerSecond = 15;
const charsToShow = Math.floor((frame / fps) * charsPerSecond);

<span>{text.slice(0, charsToShow)}</span>
```

---

## Remotion Player (Embedding in Apps)

```tsx
import { Player } from '@remotion/player';

<Player
  component={MyVideo}
  durationInFrames={300}
  fps={30}
  compositionWidth={1920}
  compositionHeight={1080}
  controls
  inputProps={{ title: 'Hello' }}
  style={{ width: '100%' }}
/>
```

---

## Installation Commands

```bash
# Create new project
npx create-video@latest

# Add packages
npx remotion add @remotion/media
npx remotion add @remotion/three
npx remotion add @remotion/lottie
npx remotion add @remotion/gif
npx remotion add @remotion/transitions
npx remotion add @remotion/google-fonts
npx remotion add @remotion/fonts
npx remotion add @remotion/layout-utils
npx remotion add @remotion/captions

# Add AI skills
npx skills add remotion-dev/skills

# Development
npm run dev

# Render
npx remotion render src/index.ts MyComposition out/video.mp4
```

---

## Resources

- **Documentation:** https://www.remotion.dev/docs
- **Templates:** https://www.remotion.dev/templates
- **Showcase:** https://www.remotion.dev/showcase
- **GitHub Skills:** https://github.com/remotion-dev/skills
- **Agent Skills:** https://agentskills.io

### Templates Available

**Free:**
- Blank, JavaScript, Hello World
- Next.js (App/Pages), React Router 7
- 3D (React Three Fiber), Skia
- Audiogram, Music Visualization
- TikTok Captions, Code Hike
- Text-to-Speech (Azure/Google)
- Prompt to Video, Prompt to Motion Graphics

**Paid:**
- Video Editor Starter
- Timeline Component
- Watercolor Map

---

## Common Patterns from JonnyBurger Examples

### Terminal Animation with Typewriter

From the Claude Code session gist, creating a macOS terminal with typewriter:

```tsx
// MacTerminal: Light theme terminal (1080x700px)
// TerminalContent: Typewriter at 15 chars/second
// Cursor: Blinking 4x10px, oscillating opacity every 0.5s
// LogoCombo: Scale-up with Easing.out(Easing.cubic) over 0.5s

// 3D transforms for perspective:
const rotateY = interpolate(frame, [0, durationInFrames], [10, -10]);
const scale = interpolate(frame, [0, durationInFrames], [0.9, 1]);

// Card flip using spring:
const flipProgress = spring({
  frame: frame - triggerFrame,
  fps,
  config: { damping: 200, stiffness: 100 },
});
const flipRotation = interpolate(flipProgress, [0, 1], [0, -90]);
```

### Spotify Wrapped Recreation

From remotion-wrapped: Parametrizable video with CLI flag overrides for text and images across three scenes.
