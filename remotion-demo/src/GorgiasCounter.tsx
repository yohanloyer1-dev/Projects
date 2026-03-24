import { AbsoluteFill, useCurrentFrame, useVideoConfig, interpolate, spring } from "remotion";

// Gorgias brand colors
const COLORS = {
  dark: "#101010",
  coral: "#FF6D62",
  peach: "#FF9780",
  cream: "#FFF9F4",
};

export const GorgiasCounter: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps, durationInFrames } = useVideoConfig();

  // Counter animation: 0% → 60% over first 3 seconds
  const counterEnd = 3 * fps; // 90 frames
  const counterValue = interpolate(
    frame,
    [0, counterEnd],
    [0, 60],
    { extrapolateRight: "clamp" }
  );

  // Background gradient reveal
  const gradientOpacity = interpolate(
    frame,
    [0, fps * 0.5],
    [0, 1],
    { extrapolateRight: "clamp" }
  );

  // Counter scale bounce when reaching 60%
  const counterScale = spring({
    frame: frame - counterEnd,
    fps,
    config: { damping: 8, stiffness: 200 },
  });
  const finalScale = frame >= counterEnd ? 1 + (counterScale - 1) * 0.1 : 1;

  // Tagline fade in after counter
  const taglineDelay = counterEnd + 10;
  const taglineOpacity = interpolate(
    frame,
    [taglineDelay, taglineDelay + 20],
    [0, 1],
    { extrapolateLeft: "clamp", extrapolateRight: "clamp" }
  );
  const taglineY = interpolate(
    frame,
    [taglineDelay, taglineDelay + 20],
    [30, 0],
    { extrapolateLeft: "clamp", extrapolateRight: "clamp" }
  );

  // Logo fade in at the end
  const logoDelay = taglineDelay + 25;
  const logoOpacity = interpolate(
    frame,
    [logoDelay, logoDelay + 15],
    [0, 1],
    { extrapolateLeft: "clamp", extrapolateRight: "clamp" }
  );
  const logoScale = spring({
    frame: frame - logoDelay,
    fps,
    config: { damping: 15, stiffness: 150 },
  });

  // Glow pulse on the percentage
  const glowIntensity = interpolate(
    (frame % 30),
    [0, 15, 30],
    [20, 35, 20]
  );

  return (
    <AbsoluteFill className="bg-[#101010] flex items-center justify-center">
      {/* Subtle gradient overlay */}
      <AbsoluteFill
        style={{ opacity: gradientOpacity }}
        className="bg-gradient-to-br from-[#101010] via-[#1a1a1a] to-[#101010]"
      />

      {/* Accent glow behind counter */}
      <div
        className="absolute rounded-full blur-3xl"
        style={{
          width: 400,
          height: 400,
          background: `radial-gradient(circle, ${COLORS.coral}30 0%, transparent 70%)`,
          opacity: interpolate(frame, [0, fps], [0, 0.6], { extrapolateRight: "clamp" }),
        }}
      />

      {/* Main content */}
      <div className="flex flex-col items-center z-10">
        {/* Counter */}
        <div
          className="font-bold text-transparent bg-clip-text"
          style={{
            fontSize: 180,
            fontFamily: "system-ui, -apple-system, sans-serif",
            fontWeight: 800,
            letterSpacing: "-0.02em",
            backgroundImage: `linear-gradient(135deg, ${COLORS.cream} 0%, ${COLORS.peach} 50%, ${COLORS.coral} 100%)`,
            transform: `scale(${finalScale})`,
            textShadow: `0 0 ${glowIntensity}px ${COLORS.coral}50`,
          }}
        >
          {Math.round(counterValue)}%
        </div>

        {/* Tagline */}
        <div
          className="text-center mt-4"
          style={{
            opacity: taglineOpacity,
            transform: `translateY(${taglineY}px)`,
          }}
        >
          <p
            className="text-3xl font-medium"
            style={{ color: COLORS.cream, letterSpacing: "0.05em" }}
          >
            Support tickets resolved by AI
          </p>
        </div>

        {/* Gorgias Logo/Text */}
        <div
          className="mt-12"
          style={{
            opacity: logoOpacity,
            transform: `scale(${Math.max(0, logoScale)})`,
          }}
        >
          <div className="flex items-center gap-3">
            {/* Simple G logo mark */}
            <div
              className="w-12 h-12 rounded-xl flex items-center justify-center font-bold text-2xl"
              style={{
                backgroundColor: COLORS.coral,
                color: COLORS.dark,
              }}
            >
              G
            </div>
            <span
              className="text-4xl font-semibold tracking-wide"
              style={{ color: COLORS.cream }}
            >
              gorgias
            </span>
          </div>
        </div>
      </div>

      {/* Bottom accent line */}
      <div
        className="absolute bottom-0 left-0 h-1"
        style={{
          width: `${(frame / durationInFrames) * 100}%`,
          background: `linear-gradient(90deg, ${COLORS.coral}, ${COLORS.peach})`,
        }}
      />
    </AbsoluteFill>
  );
};
