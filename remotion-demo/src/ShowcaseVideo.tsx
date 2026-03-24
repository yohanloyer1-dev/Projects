import React, { useRef } from "react";
import {
  AbsoluteFill,
  useCurrentFrame,
  useVideoConfig,
  interpolate,
  interpolateColors,
  spring,
  Easing,
} from "remotion";
import { ThreeCanvas } from "@remotion/three";
import { TransitionSeries, linearTiming, springTiming } from "@remotion/transitions";
import { fade } from "@remotion/transitions/fade";
import { slide } from "@remotion/transitions/slide";
import * as THREE from "three";

// ============ 3D SCENE WITH ROTATING TORUS KNOT ============
const Scene3D: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const meshRef = useRef<THREE.Mesh>(null);

  // Smooth rotation
  const rotationY = frame * 0.03;
  const rotationX = frame * 0.02;
  const rotationZ = frame * 0.01;

  // Scale animation with spring
  const scale = spring({
    frame,
    fps,
    config: { damping: 15, stiffness: 80 },
    from: 0,
    to: 1,
  });

  // Color shift over time
  const hue = (frame * 2) % 360;

  return (
    <ThreeCanvas
      width={1920}
      height={1080}
      camera={{ position: [0, 0, 5], fov: 50 }}
    >
      <ambientLight intensity={0.4} />
      <pointLight position={[10, 10, 10]} intensity={1.5} color="#00d4ff" />
      <pointLight position={[-10, -10, -5]} intensity={1} color="#a855f7" />
      <pointLight position={[0, 10, -10]} intensity={0.8} color="#ec4899" />

      {/* Main torus knot */}
      <mesh
        ref={meshRef}
        rotation={[rotationX, rotationY, rotationZ]}
        scale={scale * 1.5}
      >
        <torusKnotGeometry args={[1, 0.35, 128, 32]} />
        <meshStandardMaterial
          color={`hsl(${hue}, 70%, 60%)`}
          metalness={0.8}
          roughness={0.2}
          emissive={`hsl(${hue}, 70%, 20%)`}
          emissiveIntensity={0.5}
        />
      </mesh>

      {/* Orbiting smaller spheres */}
      {[0, 1, 2].map((i) => {
        const angle = (frame * 0.05) + (i * Math.PI * 2) / 3;
        const radius = 2.5;
        const x = Math.cos(angle) * radius;
        const z = Math.sin(angle) * radius;
        const y = Math.sin(frame * 0.03 + i) * 0.5;

        return (
          <mesh key={i} position={[x, y, z]} scale={0.2 * scale}>
            <sphereGeometry args={[1, 32, 32]} />
            <meshStandardMaterial
              color={["#00d4ff", "#a855f7", "#ec4899"][i]}
              emissive={["#00d4ff", "#a855f7", "#ec4899"][i]}
              emissiveIntensity={0.8}
              metalness={1}
              roughness={0}
            />
          </mesh>
        );
      })}
    </ThreeCanvas>
  );
};

// ============ ANIMATED TITLE ============
const AnimatedTitle: React.FC<{ text: string }> = ({ text }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  return (
    <div style={{ display: "flex", justifyContent: "center" }}>
      {text.split("").map((char, i) => {
        const charFrame = frame - i * 3;

        const y = spring({
          frame: charFrame,
          fps,
          config: { damping: 12, stiffness: 180 },
          from: 80,
          to: 0,
        });

        const opacity = interpolate(
          charFrame,
          [0, 8],
          [0, 1],
          { extrapolateLeft: "clamp", extrapolateRight: "clamp" }
        );

        const scale = spring({
          frame: charFrame,
          fps,
          config: { damping: 10, stiffness: 200 },
          from: 0.5,
          to: 1,
        });

        const rotateZ = spring({
          frame: charFrame,
          fps,
          config: { damping: 15, stiffness: 100 },
          from: -15,
          to: 0,
        });

        return (
          <span
            key={i}
            style={{
              display: "inline-block",
              fontSize: 150,
              fontWeight: 900,
              fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, sans-serif",
              color: "white",
              transform: `translateY(${y}px) scale(${scale}) rotate(${rotateZ}deg)`,
              opacity,
              textShadow: `
                0 0 60px #00d4ff,
                0 0 120px #00d4ff66,
                0 6px 0 #a855f7
              `,
              marginRight: 6,
            }}
          >
            {char}
          </span>
        );
      })}
    </div>
  );
};

// ============ GRADIENT UNDERLINE ============
const GradientUnderline: React.FC = () => {
  const frame = useCurrentFrame();

  const width = interpolate(
    frame,
    [20, 50],
    [0, 800],
    { extrapolateLeft: "clamp", extrapolateRight: "clamp", easing: Easing.out(Easing.cubic) }
  );

  const opacity = interpolate(
    frame,
    [20, 35],
    [0, 1],
    { extrapolateLeft: "clamp", extrapolateRight: "clamp" }
  );

  return (
    <div
      style={{
        width,
        height: 8,
        background: "linear-gradient(90deg, #00d4ff, #a855f7, #ec4899, #00d4ff)",
        backgroundSize: "300% 100%",
        borderRadius: 4,
        opacity,
        boxShadow: "0 0 40px #00d4ff, 0 0 80px #a855f766",
        marginTop: 40,
      }}
    />
  );
};

// ============ FEATURE CARD ============
const FeatureCard: React.FC<{
  icon: string;
  title: string;
  delay: number;
  color: string;
}> = ({ icon, title, delay, color }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  const progress = spring({
    frame: frame - delay,
    fps,
    config: { damping: 12, stiffness: 100 },
  });

  const y = interpolate(progress, [0, 1], [60, 0]);
  const opacity = interpolate(progress, [0, 0.5, 1], [0, 0.8, 1]);
  const scale = interpolate(progress, [0, 0.9, 1], [0.85, 1.03, 1]);

  return (
    <div
      style={{
        transform: `translateY(${y}px) scale(${scale})`,
        opacity,
        padding: "30px 50px",
        background: `linear-gradient(135deg, ${color}15, ${color}08)`,
        backdropFilter: "blur(20px)",
        borderRadius: 24,
        border: `2px solid ${color}50`,
        boxShadow: `0 20px 60px ${color}20, 0 0 40px ${color}15`,
        display: "flex",
        alignItems: "center",
        gap: 20,
        marginBottom: 24,
        minWidth: 400,
      }}
    >
      <span style={{ fontSize: 48 }}>{icon}</span>
      <span
        style={{
          fontSize: 38,
          fontWeight: 700,
          fontFamily: "system-ui, -apple-system, sans-serif",
          color: "white",
          textShadow: `0 0 20px ${color}`,
        }}
      >
        {title}
      </span>
    </div>
  );
};

// ============ FINAL TAGLINE ============
const FinalTagline: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  const scale = spring({
    frame,
    fps,
    config: { damping: 10, stiffness: 60 },
    from: 0.3,
    to: 1,
  });

  const opacity = interpolate(
    frame,
    [0, 15],
    [0, 1],
    { extrapolateLeft: "clamp", extrapolateRight: "clamp" }
  );

  // Glowing pulse effect
  const glowIntensity = interpolate(
    Math.sin(frame * 0.2),
    [-1, 1],
    [30, 60]
  );

  return (
    <div
      style={{
        transform: `scale(${scale})`,
        opacity,
        textAlign: "center",
      }}
    >
      <div
        style={{
          fontSize: 72,
          fontWeight: 700,
          fontFamily: "system-ui, -apple-system, sans-serif",
          color: "white",
          textShadow: `0 0 ${glowIntensity}px rgba(255,255,255,0.8), 0 0 ${glowIntensity * 2}px #00d4ff`,
          letterSpacing: "-0.02em",
        }}
      >
        Videos as Code
      </div>
      <div
        style={{
          fontSize: 28,
          fontWeight: 400,
          fontFamily: "system-ui, -apple-system, sans-serif",
          color: "rgba(255,255,255,0.7)",
          marginTop: 20,
        }}
      >
        Built with React • Rendered frame-perfect
      </div>
    </div>
  );
};

// ============ PROGRESS BAR ============
const ProgressBar: React.FC = () => {
  const frame = useCurrentFrame();
  const { durationInFrames } = useVideoConfig();

  const progress = (frame / durationInFrames) * 100;
  const barColor = interpolateColors(
    frame,
    [0, durationInFrames / 2, durationInFrames],
    ["#00d4ff", "#a855f7", "#ec4899"]
  );

  return (
    <div
      style={{
        position: "absolute",
        bottom: 40,
        left: 80,
        right: 80,
        height: 4,
        background: "rgba(255,255,255,0.1)",
        borderRadius: 2,
        overflow: "hidden",
      }}
    >
      <div
        style={{
          width: `${progress}%`,
          height: "100%",
          background: barColor,
          borderRadius: 2,
          boxShadow: `0 0 20px ${barColor}`,
        }}
      />
    </div>
  );
};

// ============ BACKGROUND ============
const AnimatedBackground: React.FC = () => {
  const frame = useCurrentFrame();
  const { durationInFrames } = useVideoConfig();

  const bgColor = interpolateColors(
    frame,
    [0, durationInFrames],
    ["#030308", "#0a0a15"]
  );

  return (
    <AbsoluteFill style={{ backgroundColor: bgColor }}>
      {/* Gradient orbs */}
      {[
        { x: "20%", y: "30%", color: "#00d4ff", size: 400 },
        { x: "80%", y: "70%", color: "#a855f7", size: 500 },
        { x: "60%", y: "20%", color: "#ec4899", size: 350 },
      ].map((orb, i) => {
        const offsetX = Math.sin(frame * 0.02 + i) * 30;
        const offsetY = Math.cos(frame * 0.015 + i) * 20;
        const opacity = interpolate(frame, [0, 30], [0, 0.25], {
          extrapolateRight: "clamp",
        });

        return (
          <div
            key={i}
            style={{
              position: "absolute",
              left: orb.x,
              top: orb.y,
              width: orb.size,
              height: orb.size,
              borderRadius: "50%",
              background: `radial-gradient(circle, ${orb.color}40, transparent 70%)`,
              transform: `translate(-50%, -50%) translate(${offsetX}px, ${offsetY}px)`,
              opacity,
              filter: "blur(60px)",
            }}
          />
        );
      })}
    </AbsoluteFill>
  );
};

// ============ SCENE COMPONENTS ============
const Scene1_3D: React.FC = () => (
  <AbsoluteFill>
    <AnimatedBackground />
    <Scene3D />
  </AbsoluteFill>
);

const Scene2_Title: React.FC = () => (
  <AbsoluteFill>
    <AnimatedBackground />
    <AbsoluteFill
      style={{
        justifyContent: "center",
        alignItems: "center",
        flexDirection: "column",
      }}
    >
      <AnimatedTitle text="REMOTION" />
      <GradientUnderline />
    </AbsoluteFill>
  </AbsoluteFill>
);

const Scene3_Features: React.FC = () => (
  <AbsoluteFill>
    <AnimatedBackground />
    <AbsoluteFill
      style={{
        justifyContent: "center",
        alignItems: "center",
        flexDirection: "column",
      }}
    >
      <FeatureCard icon="⚡" title="Programmatic" delay={0} color="#00d4ff" />
      <FeatureCard icon="⚛️" title="React-Powered" delay={8} color="#a855f7" />
      <FeatureCard icon="🎯" title="Frame-Perfect" delay={16} color="#ec4899" />
    </AbsoluteFill>
  </AbsoluteFill>
);

const Scene4_Tagline: React.FC = () => (
  <AbsoluteFill>
    <AnimatedBackground />
    <AbsoluteFill
      style={{
        justifyContent: "center",
        alignItems: "center",
      }}
    >
      <FinalTagline />
    </AbsoluteFill>
  </AbsoluteFill>
);

// ============ MAIN COMPOSITION ============
export const ShowcaseVideo: React.FC = () => {
  return (
    <AbsoluteFill style={{ backgroundColor: "#030308" }}>
      <TransitionSeries>
        {/* Scene 1: 3D Animation (0-90 frames = 3 seconds) */}
        <TransitionSeries.Sequence durationInFrames={90}>
          <Scene1_3D />
        </TransitionSeries.Sequence>

        {/* Fade transition */}
        <TransitionSeries.Transition
          presentation={fade()}
          timing={linearTiming({ durationInFrames: 15 })}
        />

        {/* Scene 2: Title (90-165 frames = ~2.5 seconds) */}
        <TransitionSeries.Sequence durationInFrames={75}>
          <Scene2_Title />
        </TransitionSeries.Sequence>

        {/* Slide transition */}
        <TransitionSeries.Transition
          presentation={slide({ direction: "from-right" })}
          timing={springTiming({ config: { damping: 200 } })}
        />

        {/* Scene 3: Features (165-240 frames = 2.5 seconds) */}
        <TransitionSeries.Sequence durationInFrames={75}>
          <Scene3_Features />
        </TransitionSeries.Sequence>

        {/* Fade transition */}
        <TransitionSeries.Transition
          presentation={fade()}
          timing={linearTiming({ durationInFrames: 15 })}
        />

        {/* Scene 4: Tagline (240-300 frames = 2 seconds) */}
        <TransitionSeries.Sequence durationInFrames={75}>
          <Scene4_Tagline />
        </TransitionSeries.Sequence>
      </TransitionSeries>

      {/* Progress bar overlay */}
      <ProgressBar />
    </AbsoluteFill>
  );
};
