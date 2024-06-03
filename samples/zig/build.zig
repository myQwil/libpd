const std = @import("std");

pub fn build(b: *std.Build) void {
	const target = b.standardTargetOptions(.{});
	const optimize = b.standardOptimizeOption(.{});

	//---------------------------------------------------------------------------
	// Add executable
	const exe = b.addExecutable(.{
		.name = "pdtest",
		.root_source_file = b.path("src/main.zig"),
		.target = target,
		.optimize = optimize,
	});
	b.installArtifact(exe);

	//---------------------------------------------------------------------------
	// Link executable with raylib
	const raylib_dep = b.dependency("raylib_zig", .{
		.target = target,
		.optimize = optimize,
	});
	exe.linkLibrary(raylib_dep.artifact("raylib"));
	exe.root_module.addImport("raylib", raylib_dep.module("raylib"));

	//---------------------------------------------------------------------------
	// Link executable with pd
	const libpd = b.path(b.fmt("../../libs/libpd.{s}", .{
		switch (exe.rootModuleTarget().os.tag) {
			.windows => "dll",
			.macos => "dylib",
			else => "so", // Linux and possibly others.
		}
	}));
	exe.addObjectFile(libpd);

	//---------------------------------------------------------------------------
	// Add run step
	const run_cmd = b.addRunArtifact(exe);
	run_cmd.step.dependOn(b.getInstallStep());
	const run_step = b.step("run", "Run the app");
	run_step.dependOn(&run_cmd.step);

	//---------------------------------------------------------------------------
	// Add test step
	const unit_tests = b.addTest(.{
		.root_source_file = b.path("src/libpd.zig"),
		.target = target,
		.optimize = optimize,
		.link_libc = true,
	});
	unit_tests.addObjectFile(libpd);
	const run_unit_tests = b.addRunArtifact(unit_tests);
	const test_step = b.step("test", "Run unit tests");
	test_step.dependOn(&run_unit_tests.step);
}
