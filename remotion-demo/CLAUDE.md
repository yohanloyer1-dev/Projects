# Remotion Skills for Claude Code

This project uses Remotion for programmatic video creation. Follow these patterns, rules, and best practices when working with this codebase.

## Project Structure

```
remotion-demo/
├── src/
│   ├── index.ts          # Entry point (registerRoot)
│   ├── Root.tsx          # Composition definitions
│   ├── MyComposition.tsx # Video components
│   └── style.css         # TailwindCSS imports
├── public/               # Static assets (fonts, images, videos)
├── remotion.config.ts    # Webpack config with TailwindCSS
└── CLAUDE.md             # This file
```

## Commands

```bash
npm run dev      # Start Remotion Studio at localhost:3000
npm run render   # Render video: npx remotion render src/index.ts CompositionId out.mp4
npm run build    # Bundle for deployment
```

---

# CRITICAL RULES

## Rule #1: Frame-Based Animation ONLY

**All animations MUST use `useCurrentFrame()` to drive motion.**

```tsx
import { useCurrentFrame, useVideoConfig, interpolate } from "remotion";

export const FadeIn: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  const opacity = interpolate(frame, [0, 2 * fps], [0, 1], {
    extrapolateRight: "clamp",
  });

  return <div style={{ opacity }}>Fading in over 2 seconds</div>;
};
```

## Rule #2: FORBIDDEN Patterns

These **WILL NOT RENDER** because Remotion renders frame-by-frame:

- `transition-*` CSS/Tailwind classes
- `animate-*` CSS/Tailwind classes
- CSS `@keyframes` animations
- `setTimeout` / `setInterval` for animations
- Any time-based animation not driven by `useCurrentFrame()`

## Rule #3: Always Clamp Interpolations

Prevent values from exceeding boundaries:

```tsx
// CORRECT - values stay within 0-1
interpolate(frame, [0, 30], [0, 1], { extrapolateRight: "clamp" });

// WRONG - opacity can exceed 1 or go negative
interpolate(frame, [0, 30], [0, 1]);
```

---

# Animation Techniques

## interpolate() - The Foundation

Maps input values to output values with optional easing:

```tsx
import { interpolate, Easing } from "remotion";

// Basic linear interpolation
const opacity = interpolate(frame, [0, 30], [0, 1], {
  extrapolateLeft: "clamp",
  extrapolateRight: "clamp",
});

// With easing
const scale = interpolate(frame, [0, 30], [0.5, 1], {
  easing: Easing.bezier(0.25, 0.1, 0.25, 1),
  extrapolateRight: "clamp",
});

// Multiple keyframes
const x = interpolate(frame, [0, 30, 60, 90], [0, 100, 100, 200]);
```

**Extrapolation Options:**
- `extend` (default): Continue interpolation beyond range
- `clamp`: Stop at boundary values
- `wrap`: Loop the values
- `identity`: Return input unchanged

## spring() - Natural Physics-Based Motion

Creates organic, bouncy animations:

```tsx
import { spring, useCurrentFrame, useVideoConfig } from "remotion";

const frame = useCurrentFrame();
const { fps } = useVideoConfig();

// Basic spring (animates 0 → 1)
const scale = spring({ frame, fps });

// Custom physics
const bounce = spring({
  frame,
  fps,
  config: {
    mass: 1,        // Lower = faster
    damping: 10,    // Higher = less bounce
    stiffness: 100, // Higher = snappier
  },
});

// With delay
const delayed = spring({ frame, fps, delay: 15 }); // 15 frame delay

// Custom range
const size = spring({ frame, fps, from: 50, to: 200 });

// Fixed duration (overrides physics)
const timed = spring({ frame, fps, durationInFrames: 30 });

// Prevent overshoot
const clamped = spring({
  frame,
  fps,
  config: { overshootClamping: true },
});
```

**Spring Presets (copy these configs):**

```tsx
// Smooth - gentle reveals, no bounce
{ damping: 200 }

// Snappy - UI elements, quick response
{ damping: 20, stiffness: 200 }

// Bouncy - playful entrances
{ damping: 8 }

// Heavy - slow, weighty movement
{ damping: 15, stiffness: 80, mass: 2 }

// Elastic - strong overshoot
{ damping: 5, stiffness: 150 }
```

## interpolateColors() - Color Transitions

```tsx
import { interpolateColors } from "remotion";

const color = interpolateColors(
  frame,
  [0, 30, 60],
  ["#ff0000", "#00ff00", "#0000ff"]
);

// Supports: hex, rgb(), rgba(), hsl(), hsla(), named colors
```

## Easing Functions

```tsx
import { Easing } from "remotion";

// Built-in easings
Easing.linear
Easing.ease           // Default CSS ease
Easing.quad           // Quadratic
Easing.cubic          // Cubic
Easing.sin            // Sinusoidal
Easing.exp            // Exponential
Easing.circle         // Circular
Easing.back           // Overshoot
Easing.elastic        // Elastic bounce
Easing.bounce         // Bouncing

// Modifiers
Easing.in(Easing.cubic)     // Ease in
Easing.out(Easing.cubic)    // Ease out
Easing.inOut(Easing.cubic)  // Ease in-out

// Custom bezier
Easing.bezier(0.25, 0.1, 0.25, 1)
```

---

# Compositions

## Basic Composition

```tsx
// src/Root.tsx
import { Composition } from "remotion";
import { MyVideo } from "./MyVideo";

export const RemotionRoot: React.FC = () => {
  return (
    <>
      <Composition
        id="MyVideo"
        component={MyVideo}
        durationInFrames={150}  // 5 seconds at 30fps
        fps={30}
        width={1920}
        height={1080}
        defaultProps={{
          title: "Hello World",
          color: "#ff0000",
        }}
      />
    </>
  );
};
```

## Multiple Compositions with Folders

```tsx
import { Composition, Folder } from "remotion";

<Folder name="Intros">
  <Composition id="Intro-1080p" ... />
  <Composition id="Intro-720p" ... />
</Folder>
<Folder name="Outros">
  <Composition id="Outro-1080p" ... />
</Folder>
```

## Stills (Single Frame Images)

```tsx
import { Still } from "remotion";

<Still
  id="Thumbnail"
  component={ThumbnailComponent}
  width={1280}
  height={720}
  defaultProps={{ title: "My Thumbnail" }}
/>
```

## Dynamic Metadata (calculateMetadata)

Compute dimensions, duration, or props before rendering:

```tsx
<Composition
  id="DynamicVideo"
  component={MyVideo}
  durationInFrames={60}
  fps={30}
  width={1920}
  height={1080}
  calculateMetadata={async ({ props, abortSignal }) => {
    // Fetch data, calculate duration, etc.
    const data = await fetch(props.apiUrl, { signal: abortSignal });
    const json = await data.json();

    return {
      durationInFrames: json.items.length * 30,
      props: { ...props, items: json.items },
    };
  }}
/>
```

---

# Sequencing & Timing

## Sequence Component

Delays when elements appear. **Inside a Sequence, useCurrentFrame() returns LOCAL frames (starting from 0).**

```tsx
import { Sequence, AbsoluteFill } from "remotion";

export const MyScene: React.FC = () => (
  <AbsoluteFill>
    {/* Appears at frame 0, lasts 30 frames */}
    <Sequence from={0} durationInFrames={30}>
      <Title />
    </Sequence>

    {/* Appears at frame 30, lasts 60 frames */}
    <Sequence from={30} durationInFrames={60}>
      <Content />
    </Sequence>

    {/* Appears at frame 60, no duration = until end */}
    <Sequence from={60}>
      <Footer />
    </Sequence>
  </AbsoluteFill>
);
```

## Series Component (No Gaps)

Automatically calculates start times:

```tsx
import { Series } from "remotion";

<Series>
  <Series.Sequence durationInFrames={30}>
    <Scene1 />
  </Series.Sequence>
  <Series.Sequence durationInFrames={45}>
    <Scene2 />
  </Series.Sequence>
  <Series.Sequence durationInFrames={30}>
    <Scene3 />
  </Series.Sequence>
</Series>
```

## Overlapping Sequences

Use negative offset:

```tsx
<Series>
  <Series.Sequence durationInFrames={60}>
    <Scene1 />
  </Series.Sequence>
  <Series.Sequence durationInFrames={60} offset={-15}>
    {/* Starts 15 frames BEFORE Scene1 ends */}
    <Scene2 />
  </Series.Sequence>
</Series>
```

---

# Transitions

Install: `npx remotion add @remotion/transitions`

```tsx
import { TransitionSeries, linearTiming, springTiming } from "@remotion/transitions";
import { fade } from "@remotion/transitions/fade";
import { slide } from "@remotion/transitions/slide";
import { wipe } from "@remotion/transitions/wipe";
import { flip } from "@remotion/transitions/flip";
import { clockWipe } from "@remotion/transitions/clock-wipe";

<TransitionSeries>
  <TransitionSeries.Sequence durationInFrames={60}>
    <Scene1 />
  </TransitionSeries.Sequence>

  <TransitionSeries.Transition
    timing={linearTiming({ durationInFrames: 20 })}
    presentation={fade()}
  />

  <TransitionSeries.Sequence durationInFrames={60}>
    <Scene2 />
  </TransitionSeries.Sequence>

  <TransitionSeries.Transition
    timing={springTiming({ config: { damping: 200 } })}
    presentation={slide({ direction: "from-left" })}
  />

  <TransitionSeries.Sequence durationInFrames={60}>
    <Scene3 />
  </TransitionSeries.Sequence>
</TransitionSeries>
```

**Important:** Transitions OVERLAP scenes. Total duration = sum of scenes - sum of transitions.

---

# Text Animations

## Typewriter Effect

**Always use string slicing. Never per-character opacity.**

```tsx
export const Typewriter: React.FC<{ text: string }> = ({ text }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  const charsPerSecond = 15;
  const charsToShow = Math.min(
    Math.floor((frame / fps) * charsPerSecond),
    text.length
  );

  return (
    <span className="font-mono text-4xl">
      {text.slice(0, charsToShow)}
      <span className="animate-none">|</span> {/* Cursor */}
    </span>
  );
};
```

## Word-by-Word Reveal

```tsx
export const WordReveal: React.FC<{ text: string }> = ({ text }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const words = text.split(" ");

  return (
    <div className="flex flex-wrap gap-2">
      {words.map((word, i) => {
        const wordDelay = i * 5; // 5 frames between words
        const opacity = interpolate(
          frame,
          [wordDelay, wordDelay + 10],
          [0, 1],
          { extrapolateLeft: "clamp", extrapolateRight: "clamp" }
        );
        const y = interpolate(
          frame,
          [wordDelay, wordDelay + 10],
          [20, 0],
          { extrapolateLeft: "clamp", extrapolateRight: "clamp" }
        );

        return (
          <span
            key={i}
            style={{ opacity, transform: `translateY(${y}px)` }}
          >
            {word}
          </span>
        );
      })}
    </div>
  );
};
```

## Character Stagger Animation

```tsx
export const StaggerText: React.FC<{ text: string }> = ({ text }) => {
  const frame = useCurrentFrame();

  return (
    <div className="flex">
      {text.split("").map((char, i) => {
        const charDelay = i * 2;
        const progress = spring({
          frame: frame - charDelay,
          fps: 30,
          config: { damping: 12 },
        });

        return (
          <span
            key={i}
            style={{
              opacity: progress,
              transform: `translateY(${(1 - progress) * 30}px)`,
            }}
          >
            {char === " " ? "\u00A0" : char}
          </span>
        );
      })}
    </div>
  );
};
```

---

# Media Assets

## Images

```tsx
import { Img, staticFile } from "remotion";

// Local image (from public/ folder)
<Img src={staticFile("logo.png")} />

// Remote image
<Img src="https://example.com/image.jpg" />

// With error handling
<Img
  src={staticFile("image.png")}
  onError={(e) => console.error("Failed to load", e)}
/>
```

## Videos

```tsx
import { OffthreadVideo, staticFile } from "remotion";

<OffthreadVideo
  src={staticFile("background.mp4")}
  volume={0.5}
  playbackRate={1}
  muted={false}
/>

// Trim video
<OffthreadVideo
  src={staticFile("video.mp4")}
  startFrom={30}  // Start at frame 30
  endAt={120}     // End at frame 120
/>
```

## Audio

```tsx
import { Audio, staticFile } from "remotion";

<Audio
  src={staticFile("music.mp3")}
  volume={0.8}
/>

// Fade audio
<Audio
  src={staticFile("music.mp3")}
  volume={(f) =>
    interpolate(f, [0, 30], [0, 1], { extrapolateRight: "clamp" })
  }
/>
```

## Fonts

```tsx
// Google Fonts (recommended)
import { loadFont } from "@remotion/google-fonts/Roboto";
const { fontFamily } = loadFont();

// In component
<div style={{ fontFamily }}>Text with Roboto</div>

// Local fonts (place in public/)
import { loadFont } from "@remotion/fonts";

loadFont({
  family: "MyFont",
  url: staticFile("fonts/MyFont.woff2"),
  weight: "400",
});
```

---

# Advanced Patterns

## Looping Animation

```tsx
const frame = useCurrentFrame();
const { fps } = useVideoConfig();

// Loop every 2 seconds
const loopDuration = 2 * fps;
const loopedFrame = frame % loopDuration;

// Continuous rotation
const rotation = (frame * 3) % 360; // 3 degrees per frame
```

## Staggered Grid Animation

```tsx
export const AnimatedGrid: React.FC = () => {
  const frame = useCurrentFrame();
  const items = Array.from({ length: 9 }, (_, i) => i);

  return (
    <div className="grid grid-cols-3 gap-4">
      {items.map((_, i) => {
        const row = Math.floor(i / 3);
        const col = i % 3;
        const delay = (row + col) * 5; // Diagonal stagger

        const scale = spring({
          frame: frame - delay,
          fps: 30,
          config: { damping: 12 },
        });

        return (
          <div
            key={i}
            className="w-20 h-20 bg-blue-500 rounded-lg"
            style={{ transform: `scale(${scale})` }}
          />
        );
      })}
    </div>
  );
};
```

## Parallax Layers

```tsx
export const ParallaxScene: React.FC = () => {
  const frame = useCurrentFrame();

  const bgX = interpolate(frame, [0, 150], [0, -50]);
  const midX = interpolate(frame, [0, 150], [0, -100]);
  const fgX = interpolate(frame, [0, 150], [0, -200]);

  return (
    <AbsoluteFill>
      <div style={{ transform: `translateX(${bgX}px)` }}>
        {/* Background layer */}
      </div>
      <div style={{ transform: `translateX(${midX}px)` }}>
        {/* Middle layer */}
      </div>
      <div style={{ transform: `translateX(${fgX}px)` }}>
        {/* Foreground layer */}
      </div>
    </AbsoluteFill>
  );
};
```

## Counter Animation

```tsx
export const Counter: React.FC<{ from: number; to: number }> = ({ from, to }) => {
  const frame = useCurrentFrame();
  const { fps, durationInFrames } = useVideoConfig();

  const value = interpolate(
    frame,
    [0, durationInFrames - 1],
    [from, to],
    { extrapolateRight: "clamp" }
  );

  return (
    <span className="text-6xl font-bold tabular-nums">
      {Math.round(value).toLocaleString()}
    </span>
  );
};
```

## Progress Bar

```tsx
export const ProgressBar: React.FC = () => {
  const frame = useCurrentFrame();
  const { durationInFrames } = useVideoConfig();

  const progress = (frame / durationInFrames) * 100;

  return (
    <div className="w-full h-2 bg-gray-700 rounded-full overflow-hidden">
      <div
        className="h-full bg-blue-500"
        style={{ width: `${progress}%` }}
      />
    </div>
  );
};
```

---

# SVG Animations

## Path Drawing (Stroke Animation)

```tsx
import { useCurrentFrame, interpolate } from "remotion";

export const DrawPath: React.FC = () => {
  const frame = useCurrentFrame();
  const strokeLength = 500; // Get this from path.getTotalLength()

  const drawProgress = interpolate(frame, [0, 60], [strokeLength, 0], {
    extrapolateRight: "clamp",
  });

  return (
    <svg viewBox="0 0 200 200">
      <path
        d="M10,100 Q100,10 190,100"
        fill="none"
        stroke="white"
        strokeWidth={4}
        strokeDasharray={strokeLength}
        strokeDashoffset={drawProgress}
      />
    </svg>
  );
};
```

---

# Layout Components

## AbsoluteFill (Full Canvas)

```tsx
import { AbsoluteFill } from "remotion";

<AbsoluteFill className="bg-black flex items-center justify-center">
  <h1>Centered Content</h1>
</AbsoluteFill>
```

## Layered Composition

```tsx
<AbsoluteFill>
  {/* Layer 1: Background */}
  <AbsoluteFill className="bg-gradient-to-br from-purple-900 to-black" />

  {/* Layer 2: Content */}
  <AbsoluteFill className="flex items-center justify-center">
    <h1>Main Content</h1>
  </AbsoluteFill>

  {/* Layer 3: Overlay */}
  <AbsoluteFill className="pointer-events-none">
    <div className="absolute bottom-4 right-4">
      <Logo />
    </div>
  </AbsoluteFill>
</AbsoluteFill>
```

---

# TailwindCSS Usage

TailwindCSS is enabled. Use freely EXCEPT:
- `transition-*` classes (FORBIDDEN)
- `animate-*` classes (FORBIDDEN)
- `duration-*` classes (FORBIDDEN for animations)

**Good patterns:**
```tsx
<div className="bg-gradient-to-r from-blue-500 to-purple-600" />
<div className="backdrop-blur-lg bg-white/10" />
<div className="shadow-2xl rounded-2xl" />
<div className="text-transparent bg-clip-text bg-gradient-to-r from-pink-500 to-yellow-500" />
```

---

# Performance Tips

1. **Premount Sequences**: Always premount to preload assets
   ```tsx
   <Sequence from={60} premountFor={30}>
     <HeavyComponent />
   </Sequence>
   ```

2. **Use `muted` for videos when audio isn't needed**: Prevents downloading entire video for audio extraction

3. **Prefer `OffthreadVideo` over `Video`**: Better performance for most cases

4. **Use `staticFile()` for local assets**: Ensures proper bundling

5. **Avoid fetching in render**: Use `calculateMetadata` for data fetching

---

# Common Video Dimensions

| Format | Width | Height | Aspect Ratio |
|--------|-------|--------|--------------|
| 1080p Landscape | 1920 | 1080 | 16:9 |
| 720p Landscape | 1280 | 720 | 16:9 |
| Instagram Square | 1080 | 1080 | 1:1 |
| Instagram Reels | 1080 | 1920 | 9:16 |
| TikTok | 1080 | 1920 | 9:16 |
| YouTube Shorts | 1080 | 1920 | 9:16 |
| Twitter Video | 1280 | 720 | 16:9 |

---

# 3D Content (React Three Fiber)

Install: `npx remotion add @remotion/three`

```tsx
import { ThreeCanvas } from "@remotion/three";
import { useCurrentFrame } from "remotion";

const My3DScene: React.FC = () => {
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

**Critical 3D Rules:**
- Use `<ThreeCanvas>` with `width` and `height` props
- Animate with `useCurrentFrame()`, **NOT** `useFrame()` from R3F (causes flickering)
- Add `layout="none"` to any `<Sequence>` inside ThreeCanvas
- Include lighting components (ambientLight, pointLight, etc.)
- Shaders and models must NOT animate by themselves

---

# Lottie Animations

Install: `npx remotion add @remotion/lottie`

```tsx
import { Lottie } from "@remotion/lottie";
import { delayRender, continueRender, staticFile } from "remotion";
import { useState, useEffect } from "react";

export const LottieAnimation: React.FC = () => {
  const [handle] = useState(() => delayRender());
  const [animationData, setAnimationData] = useState<object | null>(null);

  useEffect(() => {
    fetch(staticFile("animation.json"))
      .then((res) => res.json())
      .then((data) => {
        setAnimationData(data);
        continueRender(handle);
      });
  }, [handle]);

  if (!animationData) return null;

  return <Lottie animationData={animationData} style={{ width: 400, height: 400 }} />;
};
```

---

# Animated GIFs

Install: `npx remotion add @remotion/gif`

```tsx
import { Gif } from "@remotion/gif";
import { AnimatedImage, staticFile } from "remotion";

// For GIFs only
<Gif
  src={staticFile("animation.gif")}
  width={400}
  height={400}
  fit="contain"           // 'fill' | 'contain' | 'cover'
  playbackRate={1}
  loopBehavior="loop"     // 'loop' | 'pause-after-finish' | 'unmount-after-finish'
/>

// For APNG, AVIF, WebP (use AnimatedImage)
<AnimatedImage
  src={staticFile("animation.webp")}
  width={400}
  height={400}
  fit="contain"
/>
```

---

# Captions & Subtitles

Install: `npx remotion add @remotion/captions`

```tsx
import { createTikTokStyleCaptions } from "@remotion/captions";
import { Sequence, useVideoConfig } from "remotion";

// Create TikTok-style word-by-word captions
const { pages } = createTikTokStyleCaptions({
  captions,
  combineTokensWithinMilliseconds: 1200, // How many words per page
});

// Render captions
const { fps } = useVideoConfig();

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

**Note:** Captions are whitespace-sensitive. Use `whiteSpace: "pre"` CSS.

---

# Text Measurement

Install: `npx remotion add @remotion/layout-utils`

```tsx
import { measureText, fitText, fillTextBox } from "@remotion/layout-utils";

// Measure text dimensions
const { width, height } = measureText({
  text: "Hello",
  fontFamily: "Arial",
  fontSize: 32,
  fontWeight: "bold",
});

// Fit text to container width (returns optimal fontSize)
const { fontSize } = fitText({
  text: "Hello World",
  withinWidth: 600,
  fontFamily: "Inter",
  fontWeight: "bold",
});

// Detect text overflow
const box = fillTextBox({ maxBoxWidth: 400, maxLines: 3 });
words.forEach((word) => {
  const { exceedsBox } = box.add({
    text: word + " ",
    fontFamily: "Arial",
    fontSize: 24,
  });
  if (exceedsBox) {
    // Handle overflow
  }
});
```

**Important:** Load fonts before measuring. Use `validateFontIsLoaded: true` to catch missing fonts.

---

# DOM Measurement

Remotion applies a `scale()` transform to the video container. Use `useCurrentScale()` for accurate measurements:

```tsx
import { useCurrentScale } from "remotion";
import { useRef, useEffect, useState } from "react";

const MeasuredElement: React.FC = () => {
  const scale = useCurrentScale();
  const ref = useRef<HTMLDivElement>(null);
  const [dimensions, setDimensions] = useState({ width: 0, height: 0 });

  useEffect(() => {
    if (ref.current) {
      const rect = ref.current.getBoundingClientRect();
      setDimensions({
        width: rect.width / scale,
        height: rect.height / scale,
      });
    }
  }, [scale]);

  return <div ref={ref}>Measured content</div>;
};
```

---

# Remotion Player (Embedding in Apps)

Install: `npm install @remotion/player`

```tsx
import { Player } from "@remotion/player";
import { MyVideo } from "./MyVideo";

<Player
  component={MyVideo}
  durationInFrames={300}
  fps={30}
  compositionWidth={1920}
  compositionHeight={1080}
  controls
  autoPlay={false}
  loop={false}
  inputProps={{ title: "Hello" }}
  style={{ width: "100%" }}
/>
```

---

# Audio Visualization

Install: `npx remotion add @remotion/media-utils`

## useAudioData Hook

Fetches and caches audio waveform data for visualization.

```tsx
import { useAudioData, visualizeAudio } from "@remotion/media-utils";
import { Audio, staticFile, useCurrentFrame, useVideoConfig } from "remotion";

export const AudioVisualizer: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const audioData = useAudioData(staticFile("music.mp3"));

  if (!audioData) {
    return null; // Loading...
  }

  // Get frequency spectrum for current frame
  const spectrum = visualizeAudio({
    fps,
    frame,
    audioData,
    numberOfSamples: 32, // Must be power of 2 (16, 32, 64, 128, 256...)
  });

  return (
    <>
      <Audio src={staticFile("music.mp3")} />
      <div className="flex items-end justify-center gap-1 h-64">
        {spectrum.map((amplitude, i) => (
          <div
            key={i}
            className="w-4 bg-blue-500"
            style={{ height: `${amplitude * 100}%` }}
          />
        ))}
      </div>
    </>
  );
};
```

## visualizeAudio Parameters

| Parameter | Description |
|-----------|-------------|
| `audioData` | Data from `useAudioData()` or `getAudioData()` |
| `frame` | Current frame number |
| `fps` | Frames per second |
| `numberOfSamples` | Power of 2 (16, 32, 64...). Lower = basic levels, higher = detailed spectrum |
| `smoothing` | (optional) Averages consecutive frames for smoother transitions. Default: `true` |
| `optimizeFor` | (optional) `"accuracy"` (default) or `"speed"` |

**Returns:** Array of numbers between 0 and 1. Left side = bass (low frequencies), right side = treble (high frequencies).

## Waveform Visualization

For waveform displays (audio signal shape), use `visualizeAudioWaveform()`.

## Large Audio Files

For memory efficiency with large files, use `useWindowedAudioData()` instead of `useAudioData()`. Only works with `.wav` files.

## Audio Visualization Recipes

### Frequency Bars (Equalizer Style)

```tsx
const spectrum = visualizeAudio({ fps, frame, audioData, numberOfSamples: 16 });

<div className="flex items-end gap-1">
  {spectrum.map((amp, i) => (
    <div
      key={i}
      className="w-8 bg-gradient-to-t from-green-500 to-red-500"
      style={{ height: `${amp * 300}px` }}
    />
  ))}
</div>
```

### Circular Visualizer

```tsx
const spectrum = visualizeAudio({ fps, frame, audioData, numberOfSamples: 64 });

{spectrum.map((amp, i) => {
  const angle = (i / spectrum.length) * Math.PI * 2;
  const radius = 100 + amp * 100;
  const x = Math.cos(angle) * radius;
  const y = Math.sin(angle) * radius;

  return (
    <div
      key={i}
      className="absolute w-2 h-2 bg-white rounded-full"
      style={{ transform: `translate(${x}px, ${y}px)` }}
    />
  );
})}
```

---

# Async Data Loading (delayRender / continueRender)

When loading data, fonts, or assets asynchronously, you must pause rendering until ready.

## Basic Pattern

```tsx
import { delayRender, continueRender, cancelRender } from "remotion";
import { useState, useEffect } from "react";

export const DataDrivenVideo: React.FC = () => {
  const [handle] = useState(() => delayRender("Loading data..."));
  const [data, setData] = useState(null);

  useEffect(() => {
    fetch("/api/data")
      .then((res) => res.json())
      .then((json) => {
        setData(json);
        continueRender(handle); // Resume rendering
      })
      .catch((err) => {
        cancelRender(err); // Fail the render with error
      });
  }, [handle]);

  if (!data) return null;

  return <div>{data.title}</div>;
};
```

## Key Rules

1. **30-second timeout**: You must call `continueRender()` within 30 seconds or the render fails
2. **Component scope**: Always call `delayRender()` inside components, not at module level
3. **Multiple handles**: You can call `delayRender()` multiple times; rendering waits for all handles
4. **Error handling**: Use `cancelRender(error)` to fail gracefully with an error message

## With Retries (for flaky operations)

```tsx
const [handle] = useState(() =>
  delayRender("Fetching data...", { retries: 3 })
);
```

## Preferred: useDelayRender Hook

```tsx
import { useDelayRender } from "remotion";

const { delayRender, continueRender } = useDelayRender();
```

---

# Data Visualization

**Critical:** Disable all animations from third-party charting libraries (D3, Chart.js, etc.) - they cause flickering during render.

```tsx
// Animated bar chart with stagger
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
      className="bg-blue-500"
    />
  );
})}
```

---

# Remotion Packages Reference

Complete reference for all 35+ Remotion packages organized by category.

## Core Package

### `remotion`
The main package containing all essential components and hooks for video creation.

**Key Exports:**
- **Components:** `<Composition>`, `<Sequence>`, `<Series>`, `<AbsoluteFill>`, `<Img>`, `<Audio>`, `<OffthreadVideo>`, `<Still>`, `<Folder>`
- **Hooks:** `useCurrentFrame()`, `useVideoConfig()`, `useCurrentScale()`
- **Functions:** `interpolate()`, `spring()`, `interpolateColors()`, `staticFile()`, `delayRender()`, `continueRender()`, `registerRoot()`
- **Easing:** `Easing.linear`, `Easing.ease`, `Easing.bezier()`, etc.

```tsx
import {
  useCurrentFrame,
  useVideoConfig,
  interpolate,
  spring,
  Composition,
  Sequence,
  AbsoluteFill,
  Img,
  staticFile,
} from "remotion";
```

---

## Animation & Effects

### `@remotion/animation-utils`
CSS transform helpers for combining multiple transformations.

**Key Functions:**
- `makeTransform([...transforms])` - Combines multiple transforms into one CSS string
- `rotate(deg)`, `rotateX()`, `rotateY()`, `rotateZ()`, `rotate3d()`
- `scale(x, y?)`, `scaleX()`, `scaleY()`, `scaleZ()`, `scale3d()`
- `translate(x, y?)`, `translateX()`, `translateY()`, `translateZ()`, `translate3d()`
- `skew(x, y?)`, `skewX()`, `skewY()`
- `matrix()`, `matrix3d()`, `perspective()`

```tsx
import { makeTransform, rotate, scale, translate } from "@remotion/animation-utils";

const transform = makeTransform([
  rotate(45),
  scale(1.2),
  translate(100, 50),
]);
// Result: "rotate(45deg) scale(1.2) translate(100px, 50px)"
```

**Install:** `npx remotion add @remotion/animation-utils`

---

### `@remotion/motion-blur`
Higher-order components for motion blur and trail effects.

**Components:**
- `<Trail>` - Creates trailing duplicates with time offsets
  - `layers`: Number of duplicate layers (integer)
  - `lagInFrames`: Frame delay between layers (supports decimals)
  - `trailOpacity`: Maximum opacity for trail layers (0-1)
- `<CameraMotionBlur>` - Film camera-like motion blur
  - `shutterAngle`: Blur intensity (default: 180, range: 0-360)
  - `samples`: Quality/performance trade-off (default: 10, recommended: 5-10)

```tsx
import { Trail, CameraMotionBlur } from "@remotion/motion-blur";

// Trail effect
<Trail layers={5} lagInFrames={0.5} trailOpacity={0.6}>
  <AbsoluteFill>
    <MovingElement />
  </AbsoluteFill>
</Trail>

// Camera motion blur
<CameraMotionBlur shutterAngle={180} samples={10}>
  <AbsoluteFill>
    <FastMovingElement />
  </AbsoluteFill>
</CameraMotionBlur>
```

**Note:** Children must use absolute positioning (`<AbsoluteFill>`).

**Install:** `npx remotion add @remotion/motion-blur`

---

### `@remotion/noise`
Procedural noise generation using simplex noise algorithm.

**Functions:**
- `noise2D(seed, x, y)` - 2D noise, returns -1 to 1
- `noise3D(seed, x, y, z)` - 3D noise, returns -1 to 1
- `noise4D(seed, x, y, z, w)` - 4D noise, returns -1 to 1

```tsx
import { noise2D, noise3D } from "@remotion/noise";

const frame = useCurrentFrame();

// Organic wobble effect
const offsetX = noise2D("seed-x", frame * 0.02, 0) * 20;
const offsetY = noise2D("seed-y", 0, frame * 0.02) * 20;

// 3D noise for complex motion
const value = noise3D("my-seed", frame * 0.01, x * 0.1, y * 0.1);
```

**Use Cases:** Organic motion, particle systems, natural-looking animations.

**Install:** `npx remotion add @remotion/noise`

---

### `@remotion/transitions`
Scene transitions with timing controls.

**Components:**
- `<TransitionSeries>` - Container for scenes with transitions
- `<TransitionSeries.Sequence>` - Scene wrapper
- `<TransitionSeries.Transition>` - Transition definition

**Timing Functions:**
- `linearTiming({ durationInFrames })` - Linear progression
- `springTiming({ config })` - Physics-based timing

**Presentations:**
- `fade()` - Fade in/out (incoming fades over outgoing)
- `slide({ direction })` - Push transition (`from-left`, `from-right`, `from-top`, `from-bottom`)
- `wipe({ direction })` - Wipe over (8 directions including diagonals)
- `flip({ direction, perspective })` - 3D flip effect
- `clockWipe()` - Clock-style radial wipe

```tsx
import { TransitionSeries, linearTiming, springTiming } from "@remotion/transitions";
import { fade } from "@remotion/transitions/fade";
import { slide } from "@remotion/transitions/slide";
import { wipe } from "@remotion/transitions/wipe";
import { flip } from "@remotion/transitions/flip";

<TransitionSeries>
  <TransitionSeries.Sequence durationInFrames={60}>
    <Scene1 />
  </TransitionSeries.Sequence>
  <TransitionSeries.Transition
    timing={linearTiming({ durationInFrames: 30 })}
    presentation={fade()}
  />
  <TransitionSeries.Sequence durationInFrames={60}>
    <Scene2 />
  </TransitionSeries.Sequence>
  <TransitionSeries.Transition
    timing={springTiming({ config: { damping: 200 } })}
    presentation={slide({ direction: "from-right" })}
  />
  <TransitionSeries.Sequence durationInFrames={60}>
    <Scene3 />
  </TransitionSeries.Sequence>
</TransitionSeries>
```

**Duration Note:** Total = sum of sequences - sum of transitions (they overlap).

**Install:** `npx remotion add @remotion/transitions`

---

## Shapes & Paths

### `@remotion/shapes`
SVG shape primitives as React components.

**Components:**
- `<Circle>` - `radius`, `fill`, `stroke`, `strokeWidth`
- `<Rect>` - `width`, `height`, `fill`, `cornerRadius`
- `<Ellipse>` - `rx`, `ry`, `fill`
- `<Triangle>` - `length`, `direction` (`up`, `down`, `left`, `right`), `fill`
- `<Pie>` - `radius`, `progress`, `fill`, `rotation`
- `<Polygon>` - `points`, `fill`
- `<Star>` - `innerRadius`, `outerRadius`, `points`

```tsx
import { Circle, Rect, Triangle, Pie } from "@remotion/shapes";

<Circle radius={100} fill="blue" />
<Rect width={200} height={100} fill="red" cornerRadius={10} />
<Triangle length={100} direction="up" fill="green" />
<Pie radius={50} progress={0.75} fill="orange" />
```

**Install:** `npx remotion add @remotion/shapes`

---

### `@remotion/paths`
SVG path manipulation and animation utilities.

**Path Animation:**
- `evolvePath(progress, path)` - Animate path drawing (0 = hidden, 1 = fully drawn)
  - Returns `{ strokeDasharray, strokeDashoffset }`
- `interpolatePath(value, path1, path2)` - Morph between two paths

**Path Analysis:**
- `getLength(path)` - Get total path length
- `getPointAtLength(path, length)` - Get point coordinates at length
- `getTangentAtLength(path, length)` - Get tangent angle at length
- `getBoundingBox(path)` - Get path bounding box

**Path Manipulation:**
- `reversePath(path)` - Reverse path direction
- `scalePath(path, scaleX, scaleY)` - Scale path
- `translatePath(path, x, y)` - Translate path
- `normalizePath(path)` - Normalize to absolute coordinates
- `resetPath(path)` - Reset to origin

```tsx
import { evolvePath, interpolatePath, getLength } from "@remotion/paths";

const frame = useCurrentFrame();
const path = "M 0 0 L 100 0 L 100 100";

// Draw animation
const progress = interpolate(frame, [0, 60], [0, 1], { extrapolateRight: "clamp" });
const { strokeDasharray, strokeDashoffset } = evolvePath(progress, path);

<svg>
  <path
    d={path}
    fill="none"
    stroke="white"
    strokeDasharray={strokeDasharray}
    strokeDashoffset={strokeDashoffset}
  />
</svg>

// Path morphing
const morphedPath = interpolatePath(0.5, "M 0 0 L 100 0", "M 100 0 L 0 0");
```

**Install:** `npx remotion add @remotion/paths`

---

## 3D & Graphics

### `@remotion/three`
React Three Fiber integration for 3D content.

**Components:**
- `<ThreeCanvas>` - Main canvas component (required `width` and `height` props)

**Hooks:**
- `useVideoTexture()` - Use `<Video>` as a texture
- `useOffthreadVideoTexture()` - Use `<OffthreadVideo>` as a texture (recommended for rendering)

```tsx
import { ThreeCanvas, useVideoTexture } from "@remotion/three";
import { useCurrentFrame } from "remotion";

const My3DScene = () => {
  const frame = useCurrentFrame();
  const rotation = frame * 0.02;

  return (
    <ThreeCanvas width={1920} height={1080}>
      <ambientLight intensity={0.5} />
      <pointLight position={[10, 10, 10]} />
      <mesh rotation={[0, rotation, 0]}>
        <boxGeometry args={[2, 2, 2]} />
        <meshStandardMaterial color="hotpink" />
      </mesh>
    </ThreeCanvas>
  );
};
```

**Critical Rules:**
- Always use `useCurrentFrame()`, never `useFrame()` from R3F
- Add `layout="none"` to `<Sequence>` inside ThreeCanvas
- Include lighting components
- Set explicit `width` and `height` on `<ThreeCanvas>`

**Install:** `npx remotion add @remotion/three`

---

### `@remotion/skia`
React Native Skia integration for high-performance 2D graphics.

**Components:**
- `<SkiaCanvas>` - Wrapper for React Native Skia's Canvas with Remotion context

**Props:**
- `width` - Canvas width in pixels (required)
- `height` - Canvas height in pixels (required)
- All props from `@shopify/react-native-skia` Canvas

```tsx
import { SkiaCanvas } from "@remotion/skia";
import { Fill, Circle, Group, BlurMask } from "@shopify/react-native-skia";
import { useVideoConfig, useCurrentFrame, interpolate } from "remotion";

export const SkiaExample: React.FC = () => {
  const { width, height } = useVideoConfig();
  const frame = useCurrentFrame();

  const radius = interpolate(frame, [0, 60], [50, 150], {
    extrapolateRight: "clamp",
  });

  return (
    <SkiaCanvas width={width} height={height}>
      {/* Background */}
      <Fill color="black" />

      {/* Blurred circle */}
      <Group>
        <BlurMask blur={10} style="normal" />
        <Circle cx={width / 2} cy={height / 2} r={radius} color="cyan" />
      </Group>
    </SkiaCanvas>
  );
};
```

**Use Cases:**
- Custom shaders and GLSL effects
- Advanced gradients (linear, radial, sweep, conic)
- Blur effects and image filters
- Path drawing with Skia's powerful path API
- High-performance particle systems

**When to Use Skia vs Standard React:**
- Use **Skia** for: Complex visual effects, shaders, blur, gradients, high-performance graphics
- Use **Standard React** for: Text, images, simple shapes, layouts

**Install:** `npx remotion add @remotion/skia`

---

### `@remotion/rive`
Rive animation integration.

**Components:**
- `<RemotionRive>` - Render Rive animations synced to Remotion's timeline

```tsx
import { RemotionRive } from "@remotion/rive";

<RemotionRive
  src={staticFile("animation.riv")}
  artboard="Artboard"
  stateMachine="StateMachine"
/>
```

**Install:** `npx remotion add @remotion/rive`

---

### `@remotion/lottie`
Lottie JSON animation integration.

**Components:**
- `<Lottie>` - Render Lottie animations

**Props:**
- `animationData` - Parsed JSON animation data
- `playbackRate` - Speed multiplier
- `loop` - Enable looping
- `direction` - `1` (forward) or `-1` (backward)
- `renderer` - `"svg"` (default), `"canvas"`, or `"html"`

```tsx
import { Lottie } from "@remotion/lottie";
import { delayRender, continueRender, staticFile } from "remotion";

const [handle] = useState(() => delayRender());
const [animationData, setAnimationData] = useState(null);

useEffect(() => {
  fetch(staticFile("animation.json"))
    .then((res) => res.json())
    .then((data) => {
      setAnimationData(data);
      continueRender(handle);
    });
}, []);

{animationData && (
  <Lottie
    animationData={animationData}
    style={{ width: 400, height: 400 }}
  />
)}
```

**Install:** `npx remotion add @remotion/lottie`

---

### `@remotion/gif`
Animated GIF rendering synchronized with Remotion's frame.

**Components:**
- `<Gif>` - Render GIFs synced to `useCurrentFrame()`

**Props:**
- `src` - GIF source URL or staticFile
- `width`, `height` - Dimensions
- `fit` - `"fill"`, `"contain"`, `"cover"`
- `playbackRate` - Speed multiplier (1 = normal)
- `loopBehavior` - `"loop"`, `"pause-after-finish"`, `"unmount-after-finish"`
- `onLoad` - Callback with GIF metadata

```tsx
import { Gif } from "@remotion/gif";

<Gif
  src={staticFile("animation.gif")}
  width={400}
  height={400}
  fit="contain"
  playbackRate={1}
  loopBehavior="loop"
/>
```

**Note:** For APNG, AVIF, WebP use `<AnimatedImage>` from core `remotion` package.

**Install:** `npx remotion add @remotion/gif`

---

### `@remotion/animated-emoji`
Google Fonts Animated Emoji integration.

**Components:**
- `<AnimatedEmoji>` - Render animated emojis

**Props:**
- `emoji` - Emoji name (e.g., `"smile"`, `"fire"`, `"heart"`)
- `scale` - Resolution: `0.5` (512px), `1` (1024px, default), `2` (2048px)

```tsx
import { AnimatedEmoji } from "@remotion/animated-emoji";

<AnimatedEmoji emoji="fire" scale={1} />
<AnimatedEmoji emoji="heart" />
<AnimatedEmoji emoji="thumbs-up" scale={2} />
```

**Setup Required:** Copy emoji assets from `@remotion/animated-emoji/public` to your project's `public` folder.

**License:** Emoji assets under CC BY 4.0.

**Install:** `npx remotion add @remotion/animated-emoji`

---

## Text & Fonts

### `@remotion/google-fonts`
Easy Google Fonts loading.

**Usage:**
```tsx
// Import specific font
import { loadFont } from "@remotion/google-fonts/Inter";
import { loadFont } from "@remotion/google-fonts/Roboto";
import { loadFont } from "@remotion/google-fonts/Poppins";

const { fontFamily } = loadFont({
  weights: ["400", "700"],
  subsets: ["latin"],
});

<div style={{ fontFamily }}>Text with Inter</div>
```

**Install:** `npx remotion add @remotion/google-fonts`

---

### `@remotion/fonts`
Local font loading utility.

**Functions:**
- `loadFont({ family, url, weight, style })` - Load local font files

```tsx
import { loadFont } from "@remotion/fonts";
import { staticFile } from "remotion";

loadFont({
  family: "CustomFont",
  url: staticFile("fonts/CustomFont.woff2"),
  weight: "400",
});

// Use in component
<div style={{ fontFamily: "CustomFont" }}>Custom text</div>
```

**Install:** `npx remotion add @remotion/fonts`

---

### `@remotion/layout-utils`
Text measurement and layout utilities.

**Functions:**
- `measureText({ text, fontFamily, fontSize, ... })` - Returns `{ width, height }`
- `fitText({ text, withinWidth, fontFamily, ... })` - Returns optimal `{ fontSize }`
- `fillTextBox({ maxBoxWidth, maxLines })` - Detect text overflow

```tsx
import { measureText, fitText, fillTextBox } from "@remotion/layout-utils";

// Measure text dimensions
const { width, height } = measureText({
  text: "Hello World",
  fontFamily: "Arial",
  fontSize: 32,
  fontWeight: "bold",
});

// Auto-fit text to width
const { fontSize } = fitText({
  text: "Long text that needs to fit",
  withinWidth: 600,
  fontFamily: "Inter",
});

// Detect overflow
const box = fillTextBox({ maxBoxWidth: 400, maxLines: 3 });
words.forEach((word) => {
  const { exceedsBox } = box.add({
    text: word + " ",
    fontFamily: "Arial",
    fontSize: 24,
  });
});
```

**Important:** Font must be loaded before measuring. Use `validateFontIsLoaded: true` option.

**Install:** `npx remotion add @remotion/layout-utils`

---

## Media

### `@remotion/media-utils`
Media metadata and audio visualization utilities.

**Functions:**
- `getVideoMetadata(src)` - Get video duration, dimensions, fps
- `getAudioDurationInSeconds(src)` - Get audio duration
- `useAudioData(src)` - Hook for audio waveform data (Remotion-only)
- `visualizeAudio({ fps, frame, audioData, numberOfSamples })` - Generate visualization data

```tsx
import { getVideoMetadata, getAudioDurationInSeconds, useAudioData, visualizeAudio } from "@remotion/media-utils";

// In calculateMetadata
const metadata = await getVideoMetadata(staticFile("video.mp4"));
const duration = await getAudioDurationInSeconds(staticFile("audio.mp3"));

// Audio visualization
const audioData = useAudioData(staticFile("music.mp3"));
if (audioData) {
  const visualization = visualizeAudio({
    fps,
    frame,
    audioData,
    numberOfSamples: 256,
  });
}
```

**Install:** `npx remotion add @remotion/media-utils`

---

### `@remotion/media-parser`
Parse video/audio files for metadata and samples.

**Supported Formats:** MP4, MOV, WebM, MKV, AVI, M3U8, TS, MP3, WAV, AAC, M4A, FLAC

**Features:**
- Extract metadata from 20+ fields
- Extract compressed samples for WebCodecs
- Works in browser, Node.js, and Bun
- Zero dependencies
- Pausable, resumable, cancellable

**Install:** `npx remotion add @remotion/media-parser`

---

### `@remotion/webcodecs`
Browser-based video conversion using WebCodecs API.

**Features:**
- Format conversion (MP4, WebM, MOV, MKV, MP3, FLAC, WAV)
- Video rotation and pixel manipulation
- Frame extraction
- Audio extraction
- MediaRecorder video repair
- GPU-accelerated processing

**Note:** Marked as unstable; Remotion plans to transition to Mediabunny.

**Install:** `npx remotion add @remotion/webcodecs`

---

## Speech & Transcription

### `@remotion/install-whisper-cpp`
Local Whisper.cpp installation and transcription.

**Functions:**
- `installWhisperCpp()` - Install Whisper.cpp locally
- `downloadWhisperModel(model)` - Download model (e.g., `"medium.en"`)
- `transcribe({ inputPath, model, ... })` - Transcribe audio with timestamps
- `toCaptions(transcription)` - Convert to Remotion caption format

```tsx
import { installWhisperCpp, downloadWhisperModel, transcribe } from "@remotion/install-whisper-cpp";

// Setup (run once)
await installWhisperCpp({ version: "1.5.4" });
await downloadWhisperModel({ model: "medium.en" });

// Transcribe
const result = await transcribe({
  inputPath: "audio.wav",
  model: "medium.en",
  tokenLevelTimestamps: true,
});
```

**Use Cases:** Offline transcription, privacy-sensitive audio processing.

**Install:** `npx remotion add @remotion/install-whisper-cpp`

---

### `@remotion/openai-whisper`
OpenAI Whisper API integration.

**Functions:**
- Transform OpenAI Whisper API output to Remotion Caption format

```tsx
import { openAiWhisperToCaptions } from "@remotion/openai-whisper";

const whisperResponse = await openai.audio.transcriptions.create({
  file: audioFile,
  model: "whisper-1",
  response_format: "verbose_json",
  timestamp_granularities: ["word"],
});

const captions = openAiWhisperToCaptions(whisperResponse);
```

**Install:** `npx remotion add @remotion/openai-whisper`

---

### `@remotion/whisper-web`
Browser-based Whisper transcription via WebAssembly.

**Features:**
- Client-side transcription (no server needed)
- Privacy-preserving
- Multiple model sizes
- Progress tracking

**Requirements:** `SharedArrayBuffer` support (requires CORS headers).

**Install:** `npx remotion add @remotion/whisper-web`

---

### `@remotion/captions`
Caption and subtitle utilities.

**Functions:**
- `createTikTokStyleCaptions({ captions, combineTokensWithinMilliseconds })` - TikTok-style word-by-word captions

```tsx
import { createTikTokStyleCaptions } from "@remotion/captions";

const { pages } = createTikTokStyleCaptions({
  captions,
  combineTokensWithinMilliseconds: 1200,
});

// Render pages
{pages.map((page, i) => (
  <Sequence
    key={i}
    from={Math.floor((page.startMs / 1000) * fps)}
    durationInFrames={Math.ceil(((page.endMs - page.startMs) / 1000) * fps)}
  >
    <div style={{ whiteSpace: "pre" }}>{page.text}</div>
  </Sequence>
))}
```

**Note:** Use `whiteSpace: "pre"` CSS for proper spacing.

**Install:** `npx remotion add @remotion/captions`

---

## Rendering & Deployment

### `@remotion/renderer`
Server-side video rendering.

**Functions:**
- `bundle({ entryPoint })` - Bundle project with Webpack
- `selectComposition({ serveUrl, id })` - Get composition config
- `renderMedia({ composition, serveUrl, codec, outputLocation, ... })` - Render video/audio
- `renderFrames()` - Render frames individually
- `stitchFramesToVideo()` - Combine frames into video

**Codecs:** `h264`, `h265`, `vp8`, `vp9`, `prores`, `gif`, `mp3`, `aac`, `wav`

```tsx
import { bundle, selectComposition, renderMedia } from "@remotion/renderer";

const bundled = await bundle({ entryPoint: "./src/index.ts" });
const composition = await selectComposition({
  serveUrl: bundled,
  id: "MyVideo",
});

await renderMedia({
  composition,
  serveUrl: bundled,
  codec: "h264",
  outputLocation: "out/video.mp4",
  inputProps: { title: "Hello" },
  onProgress: ({ progress }) => console.log(`${Math.round(progress * 100)}%`),
});
```

**Install:** `npm install @remotion/renderer`

---

### `@remotion/lambda`
AWS Lambda serverless rendering.

**Features:**
- Pay-per-use pricing
- Parallel rendering across multiple Lambda functions
- Max ~80 minutes at Full HD (Lambda timeout limit)
- ~5GB output limit

**Architecture:**
1. Deploy to S3
2. Invoke Lambda functions in parallel
3. Stitch chunks and upload final output

```tsx
import { renderMediaOnLambda, getRenderProgress } from "@remotion/lambda";

const { renderId, bucketName } = await renderMediaOnLambda({
  region: "us-east-1",
  functionName: "remotion-render",
  composition: "MyVideo",
  inputProps: {},
  codec: "h264",
});

// Check progress
const progress = await getRenderProgress({
  renderId,
  bucketName,
  region: "us-east-1",
  functionName: "remotion-render",
});
```

**Install:** `npm install @remotion/lambda`

---

### `@remotion/cloudrun`
Google Cloud Run serverless rendering (Alpha).

**Features:**
- Pay-per-use on GCP
- Up to 60-minute timeout
- Up to 32GB memory, 8 vCPU
- Output to Cloud Storage

**Install:** `npm install @remotion/cloudrun`

---

### `@remotion/player`
Embed Remotion videos in React apps.

**Components:**
- `<Player>` - Embeddable video player

**Props:**
- `component` - Video component (not wrapped in `<Composition>`)
- `durationInFrames`, `fps`, `compositionWidth`, `compositionHeight` - Required
- `controls` - Show playback controls
- `autoPlay`, `loop` - Playback options
- `playbackRate` - Speed (-4 to 4, excluding 0)
- `inputProps` - Props passed to component

**Ref Methods:**
- `play()`, `pause()`, `toggle()`
- `seekTo(frame)`
- `getCurrentFrame()`
- `isPlaying()`

```tsx
import { Player, PlayerRef } from "@remotion/player";

const playerRef = useRef<PlayerRef>(null);

<Player
  ref={playerRef}
  component={MyVideo}
  durationInFrames={300}
  fps={30}
  compositionWidth={1920}
  compositionHeight={1080}
  controls
  autoPlay={false}
  loop
  inputProps={{ title: "Hello" }}
  style={{ width: "100%" }}
/>

// Control programmatically
playerRef.current?.play();
playerRef.current?.seekTo(60);
```

**Install:** `npm install @remotion/player`

---

## Build & Configuration

### `@remotion/bundler`
Webpack bundling for server-side rendering.

**Functions:**
- `bundle({ entryPoint })` - Bundle Remotion project

```tsx
import { bundle } from "@remotion/bundler";

const bundled = await bundle({
  entryPoint: "./src/index.ts",
  webpackOverride: (config) => config,
});
```

**Install:** Included with `@remotion/renderer`

---

### `@remotion/cli`
Command-line interface for Remotion.

**Commands:**
- `npx remotion dev` - Start Studio
- `npx remotion render <entry> <compositionId> <output>` - Render video
- `npx remotion still <entry> <compositionId> <output>` - Render still
- `npx remotion add <package>` - Add Remotion package
- `npx remotion benchmark` - Performance testing

**Install:** Included with `remotion`

---

### `@remotion/studio`
Development environment and preview server.

**Features:**
- Live preview at localhost:3000
- Timeline scrubbing
- Composition selector
- Props editor
- Render queue

**Install:** Included with `remotion`

---

### `@remotion/tailwind` / `@remotion/tailwind-v4`
TailwindCSS integration.

**Setup (v4):**
```ts
// remotion.config.ts
import { enableTailwind } from "@remotion/tailwind-v4";

Config.overrideWebpackConfig((config) => enableTailwind(config));
```

**Setup (v3):**
```ts
// remotion.config.ts
import { enableTailwind } from "@remotion/tailwind";

Config.overrideWebpackConfig((config) => enableTailwind(config));
```

**Remember:** `transition-*` and `animate-*` classes are FORBIDDEN.

**Install:** `npx remotion add @remotion/tailwind` or `@remotion/tailwind-v4`

---

### `@remotion/enable-scss`
SCSS/Sass support.

**Setup:**
```ts
// remotion.config.ts
import { enableScss } from "@remotion/enable-scss";

Config.overrideWebpackConfig((config) => enableScss(config));
```

**Install:** `npx remotion add @remotion/enable-scss`

---

## Utilities

### `@remotion/zod-types`
Zod schema types for type-safe props.

**Purpose:** Define validated, type-safe component props using Zod schemas.

```tsx
import { z } from "zod";
import { zColor } from "@remotion/zod-types";

const schema = z.object({
  title: z.string(),
  color: zColor(),
  count: z.number().min(1).max(10),
});

type Props = z.infer<typeof schema>;
```

**Install:** `npx remotion add @remotion/zod-types`

---

### `@remotion/licensing`
License validation and usage tracking.

**Purpose:** Track render usage for Company License holders.

```tsx
import { renderMedia } from "@remotion/renderer";

await renderMedia({
  // ... other options
  licenseKey: "your-license-key",
});
```

**Install:** Included with rendering packages

---

### `@remotion/preload`
Asset preloading utilities.

**Functions:**
- `preloadVideo(src)` - Preload video
- `preloadAudio(src)` - Preload audio
- `preloadImage(src)` - Preload image
- `preloadFont(src)` - Preload font

```tsx
import { preloadVideo, preloadAudio } from "@remotion/preload";

// Preload in useEffect or calculateMetadata
preloadVideo(staticFile("video.mp4"));
preloadAudio(staticFile("music.mp3"));
```

**Install:** `npx remotion add @remotion/preload`

---

## Quick Installation Reference

```bash
# Animation & Effects
npx remotion add @remotion/animation-utils
npx remotion add @remotion/motion-blur
npx remotion add @remotion/noise
npx remotion add @remotion/transitions

# Shapes & Paths
npx remotion add @remotion/shapes
npx remotion add @remotion/paths

# 3D & Graphics
npx remotion add @remotion/three
npx remotion add @remotion/skia
npx remotion add @remotion/rive
npx remotion add @remotion/lottie
npx remotion add @remotion/gif
npx remotion add @remotion/animated-emoji

# Text & Fonts
npx remotion add @remotion/google-fonts
npx remotion add @remotion/fonts
npx remotion add @remotion/layout-utils

# Media
npx remotion add @remotion/media-utils
npx remotion add @remotion/media-parser
npx remotion add @remotion/webcodecs
npx remotion add @remotion/preload

# Speech & Transcription
npx remotion add @remotion/install-whisper-cpp
npx remotion add @remotion/openai-whisper
npx remotion add @remotion/whisper-web
npx remotion add @remotion/captions

# Rendering
npm install @remotion/renderer
npm install @remotion/lambda
npm install @remotion/cloudrun
npm install @remotion/player

# Build Tools
npx remotion add @remotion/tailwind
npx remotion add @remotion/tailwind-v4
npx remotion add @remotion/enable-scss
npx remotion add @remotion/zod-types
```

---

# Resources & Templates

## Official Free Templates (20+)

| Template | Description | Use Case |
|----------|-------------|----------|
| **Blank** | Empty canvas | Custom projects |
| **Hello World** | Simple animation | Learning basics |
| **JavaScript** | Plain JS starter | Non-TypeScript projects |
| **Next.js (App dir)** | SaaS video generation | Web apps with video rendering |
| **Next.js + TailwindCSS** | SaaS with styling | Styled web apps |
| **React Router 7** | SaaS setup | Modern React apps |
| **3D** | React Three Fiber | 3D animations |
| **Skia** | React Native Skia | High-performance 2D graphics |
| **Recorder** | Video production tool | Recording/editing |
| **Stills** | Dynamic PNG/JPEG | Thumbnails, social images |
| **Render Server** | Express.js backend | API-based rendering |
| **Audiogram** | Waveform + text | Podcast clips |
| **Music Visualization** | Audio reactive | Music videos |
| **TikTok** | Word-by-word captions | Social media shorts |
| **Code Hike** | Beautiful code | Dev tutorials |
| **Overlay** | Video overlays | Streaming, editing |
| **Stargazer** | GitHub star celebration | Developer marketing |
| **Text-to-Speech (Azure)** | TTS videos | Automated narration |
| **Text-to-Speech (Google)** | Google TTS | Automated narration |
| **Prompt to Video** | AI story creation | AI-generated content |
| **Prompt to Motion Graphics** | AI code generation | AI-powered design |

## Paid Templates

| Template | Description |
|----------|-------------|
| **Editor Starter** | Video editor boilerplate |
| **Timeline** | Copy-paste timeline component |
| **Watercolor Map** | 2D animated travel maps |

## Create from Template

```bash
# Interactive template selector
npx create-video@latest

# Specific template
npx create-video@latest --template=next-app
npx create-video@latest --template=audiogram
npx create-video@latest --template=tiktok
npx create-video@latest --template=3d
```

## Links

- **Documentation:** https://www.remotion.dev/docs
- **Templates:** https://www.remotion.dev/templates
- **Showcase:** https://www.remotion.dev/showcase
- **GitHub Skills:** https://github.com/remotion-dev/skills
- **Agent Skills:** https://agentskills.io

---

# API Reference

- Full docs: https://www.remotion.dev/docs/
- Append `.md` to any doc URL for raw markdown
- Examples: https://www.remotion.dev/docs/resources

---

# Common Recipes

## TikTok-Style Captions

```tsx
import { createTikTokStyleCaptions } from "@remotion/captions";
import { Sequence, useVideoConfig } from "remotion";

// Your captions array from transcription
const captions = [
  { text: " Hello", startMs: 0, endMs: 500 },
  { text: " world", startMs: 500, endMs: 1000 },
  // ...
];

export const CaptionedVideo: React.FC = () => {
  const { fps } = useVideoConfig();

  const { pages } = createTikTokStyleCaptions({
    captions,
    combineTokensWithinMilliseconds: 800, // Words per page
  });

  return (
    <>
      {pages.map((page, i) => (
        <Sequence
          key={i}
          from={Math.floor((page.startMs / 1000) * fps)}
          durationInFrames={Math.ceil(((page.endMs - page.startMs) / 1000) * fps)}
        >
          <div
            className="absolute bottom-20 left-0 right-0 text-center"
            style={{ whiteSpace: "pre" }}
          >
            <span className="text-4xl font-bold text-white drop-shadow-lg">
              {page.tokens.map((token, j) => (
                <span
                  key={j}
                  className={token.isActive ? "text-yellow-400" : "text-white"}
                >
                  {token.text}
                </span>
              ))}
            </span>
          </div>
        </Sequence>
      ))}
    </>
  );
};
```

## Logo Reveal with Path Drawing

```tsx
import { evolvePath } from "@remotion/paths";
import { useCurrentFrame, interpolate } from "remotion";

export const LogoReveal: React.FC<{ path: string }> = ({ path }) => {
  const frame = useCurrentFrame();

  const progress = interpolate(frame, [0, 60], [0, 1], {
    extrapolateRight: "clamp",
  });

  const { strokeDasharray, strokeDashoffset } = evolvePath(progress, path);

  // Fill opacity fades in after drawing completes
  const fillOpacity = interpolate(frame, [50, 80], [0, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  return (
    <svg viewBox="0 0 100 100">
      <path
        d={path}
        fill={`rgba(255, 255, 255, ${fillOpacity})`}
        stroke="white"
        strokeWidth={2}
        strokeDasharray={strokeDasharray}
        strokeDashoffset={strokeDashoffset}
      />
    </svg>
  );
};
```

## Intro Sequence Pattern

```tsx
import { TransitionSeries, linearTiming } from "@remotion/transitions";
import { fade } from "@remotion/transitions/fade";
import { slide } from "@remotion/transitions/slide";

export const IntroSequence: React.FC = () => {
  return (
    <TransitionSeries>
      {/* Logo reveal */}
      <TransitionSeries.Sequence durationInFrames={90}>
        <LogoScene />
      </TransitionSeries.Sequence>

      <TransitionSeries.Transition
        timing={linearTiming({ durationInFrames: 20 })}
        presentation={fade()}
      />

      {/* Title card */}
      <TransitionSeries.Sequence durationInFrames={60}>
        <TitleScene />
      </TransitionSeries.Sequence>

      <TransitionSeries.Transition
        timing={linearTiming({ durationInFrames: 15 })}
        presentation={slide({ direction: "from-right" })}
      />

      {/* Main content */}
      <TransitionSeries.Sequence durationInFrames={300}>
        <MainContent />
      </TransitionSeries.Sequence>
    </TransitionSeries>
  );
};
```
